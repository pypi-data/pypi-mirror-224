#! /bin/python3

import os
import pandas as pd
import time as t
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
import queue
import time
from pathlib import Path


def partitioning(k,dataset,attributes,sct_method='full_order_CL',W=5,cutoff=60):
    dist_matrix = generate_dist_matrix(dataset,attributes)
    cont_matrix = generate_cont_matrix(dataset)
    sct = SCT(dataset[attributes],contiguity_matrix=cont_matrix,distance_matrix=dist_matrix,method=sct_method)
    h_tot, regions, regions_h, proved_exact, edges_removed, partition_time = sct.partition(k,'mdd',W,cutoff)
    return Regionalization_result(h_tot, regions, regions_h, proved_exact, partition_time)

def generate_dist_matrix(df, cols, dist_deg=2):
    indexes = df.index
    dist_matrix = pd.DataFrame(0, index=indexes, columns=indexes)
    for i in range(len(indexes) - 1):
        index1 = indexes[i]
        for j in range(i + 1, len(indexes)):
            index2 = indexes[j]
            dist = 0
            for col in cols:
                dist += (df.loc[index1, col] - df.loc[index2, col]) ** dist_deg
            dist_matrix.loc[index1, index2] = dist
            dist_matrix.loc[index2, index1] = dist
    return dist_matrix


def generate_cont_matrix(df):
    contiguity_matrix = pd.DataFrame(0, index=df.index, columns=df.index)
    for index, row in df.iterrows():
        for n in row.neighbors:
            contiguity_matrix.loc[index, n] = 1
    return contiguity_matrix

def  solve_regionalization(vertex, neighbors, id2edge, k, w, timeout):
    '''
    '''
    with open('vertices.txt', 'w') as f:
        for j,vs in enumerate(vertex):
            for i,v in enumerate(vs):
                f.write(str(v))
                if i < len(vs) - 1:
                    f.write(' ')
            if j < len(vertex) -1:
                f.write('\n')
    with open('neighbors.txt', 'w') as f:
        for j,ns in enumerate(neighbors):
            for i,n in enumerate(ns):
                f.write(str(n))
                if i < len(ns) - 1:
                    f.write(' ')
            if j < len(neighbors) -1:
                f.write('\n')
    with open('id2edge.txt', 'w') as f:
        for j,(s, d) in enumerate(id2edge):
            f.write(str(s))
            f.write(' ')
            f.write(str(d))
            if j < len(id2edge) -1:
                f.write('\n')
    os.system("./target/release/regiorust -v vertices.txt -n neighbors.txt -i id2edge.txt -k {} -w {} -t {}".format(
        k, w, timeout))
    with open('result.txt') as f:
        line = f.read().split(' | ')
        proved_exact = line[0]
        h_tot = float(line[1])
        edges_removed = []
        if len(line[2]) > 2:
            for edge in line[2][2:-2].split('), ('):
                vertices = edge.split(', ')
                edges_removed.append((int(vertices[0]),int(vertices[1])))
    return h_tot, proved_exact, edges_removed


class Cluster:
    def __init__(self,index,edges):
        self.name = index
        self.v = [index]
        self.e = edges
        self.on = True

    def get_name(self):
        return self.name

    def get_e(self):
        return self.e

    def get_v(self):
        return self.v

    def find_shortest_edge(self,cluster):
        best_u = self.v[0]
        best_dist = float('inf')
        best_v = cluster.get_v()[0]
        for v in cluster.get_v():
            if v in self.e:
                for u in self.e[v].keys():
                    if self.e[v][u] < best_dist:
                        best_u = u
                        best_v = v
                        best_dist = self.e[v][u]
        return (best_u,best_v),best_dist

    def go_off(self):
        self.on = False

    def grow(self,cluster):
        self.v += cluster.get_v()
        for e in cluster.get_e().keys():
            if e in self.e:
                for u in cluster.get_e()[e].keys():
                    self.e[e][u] = cluster.get_e()[e][u]
            else:
                self.e[e] = cluster.get_e()[e]

    def __eq__(self, other):
        return self.name == other.name()



class SCT:
    def __init__(self, data, contiguity_matrix=None, distance_matrix=None, method = 'full_order_CL',talk=False):
        self.method = method
        self.talk = talk
        self.times = {}
        if isinstance(data,str):
            self.vertices = pd.read_json('./data/'+data+'/'+data+'.json')
            self.vertices = self.vertices.sort_index()
            self.name = data
            if method == 'full_order_CL':
                if Path('./data/'+data+'/'+data+'_sct.csv').is_file():
                    self.edges, self.neighbors = self.read_file()
                else:
                    self.cont_m = pd.read_json('./data/' + data + '/' + data + '_cont.json')
                    self.dist = pd.read_json('./data/' + data + '/' + data + '_dist.json')
                    self.edges, self.neighbors = self.find_SCT_full_order_CL()
            elif method == 'MST':
                if Path('./data/'+data+'/'+data+'_mst.csv').is_file():
                    self.edges, self.neighbors = self.read_file()
                else:
                    self.cont_m = pd.read_json('./data/' + data + '/' + data + '_cont.json')
                    self.dist = pd.read_json('./data/' + data + '/' + data + '_dist.json')
                    self.edges, self.neighbors = self.find_MST()
            else:
                raise Exception('Wrong SCT method, must be full_order_CL or MST')
        else:
            self.cont_m = contiguity_matrix
            self.dist = distance_matrix
            self.vertices = data
            if method == 'full_order_CL':
                self.edges, self.neighbors = self.find_SCT_full_order_CL()
            elif method == 'MST':
                self.edges, self.neighbors = self.find_MST()
            else:
                raise Exception('Wrong SCT method, must be full_order_CL or MST')

    def create_clusters(self):
        clusters = {}
        for i in self.cont_m.index:
            e = {}
            for j in self.cont_m.index:
                if i != j and self.cont_m.loc[i,j] > 0:
                    e[j] = {i: self.dist.loc[i,j]}
            clusters[i] = Cluster(i, e)
        return clusters

    def sorted_full_order_edges(self):
        FullO_E = {}
        indexes = self.dist.index
        for i in range(len(indexes) - 1):
            index1 = indexes[i]
            for j in range(i + 1, len(indexes)):
                index2 = indexes[j]
                dist = self.dist.loc[index1,index2]
                if index1 < index2:
                    FullO_E[(index1, index2)] = dist
                else:
                    FullO_E[(index2, index1)] = dist
        sorted_FullO_E = {k: v for k, v in sorted(FullO_E.items(), key=lambda item: item[1])}
        return sorted_FullO_E

    def merge(self,l,m,clusters,cont_C,dist_C):
        clusters[m].go_off()
        clusters[l].grow(clusters[m])
        for v in clusters[m].get_v():
            clusters[v] = clusters[l]
        cont_C[l] = cont_C[[l,m]].max(axis=1)
        cont_C.loc[l] = cont_C.loc[[l, m]].max(axis=0)
        dist_C[l] = dist_C[[l, m]].max(axis=1)
        dist_C.loc[l] = dist_C.loc[[l, m]].max(axis=0)

    def find_MST(self):
        if self.talk:
            print('start MST')
        t1 = t.time()
        FirstO = self.cont_m.values * self.dist.values
        MST = minimum_spanning_tree(FirstO).toarray()
        neighbors = {v: [] for v in self.vertices.index}
        edges = {}
        for i, row in enumerate(MST):
            for j, el in enumerate(row):
                if el > 0:
                    neighbors[i].append(j)
                    neighbors[j].append(i)
                    edges[min(i,j),max(i,j)] = el
        t2 = t.time()
        self.times['SCT'] = t2 - t1
        self.times['sort FuO edges'] = 0.0
        if self.talk:
            print('end MST ' + str(self.times['SCT']))
        return list(edges.keys()), neighbors

    def find_SCT_full_order_CL(self):

        if self.talk:
            print('start sort full_order')
        t1 = t.time()
        FullO_E = self.sorted_full_order_edges()
        t2 = t.time()
        self.times['sort FuO edges'] = t2-t1
        if self.talk:
            print('end sort full order ' + str(self.times['sort FuO edges']))

        if self.talk:
            print('start SCT')
        i = 0
        edges = {}
        neighbors = {v : [] for v in self.vertices.index}
        cont_C = self.cont_m.copy()
        dist_C = self.dist.copy()
        clusters = self.create_clusters()
        t1 = t.time()
        for (u,v) in FullO_E.keys():
            l, m = clusters[u].get_name(), clusters[v].get_name()
            if l != m and cont_C[l][m] != 0 and FullO_E[(u,v)] >= dist_C[l][m]:
                e,cost = clusters[u].find_shortest_edge(clusters[v])
                e = tuple(sorted(e))
                edges[e] = cost
                self.merge(l,m,clusters,cont_C,dist_C) # changing clusters, changing contiguity and changing dist_C
                neighbors[e[0]] += [e[1]]
                neighbors[e[1]] += [e[0]]
                i += 1
        t2 = t.time()
        self.times['SCT'] = t2-t1
        if self.talk:
            print('stop SCT ' + str(self.times['SCT']))
        return list(edges.keys()), neighbors

    def compute_h(self, region):
        mean = np.array(self.vertices.loc[region].mean())
        h = 0.
        for vertice in region:
            h += np.sum(np.square(np.array(self.vertices.loc[vertice]) - mean))
        return h

    def dfs_connected_vertex(self, vertice, edges):
        visited = set()
        q = queue.Queue()
        visited.add(vertice)
        q.put(vertice)
        while not q.empty():
            v = q.get()
            for n in self.neighbors[v]:
                e = tuple(sorted((v,n)))
                if edges[e] and n not in visited:
                    visited.add(n)
                    q.put(n)
        return list(visited)

    def partition(self,k,method,W=5,cutoff=60):
        if self.talk:
            print("== partition started ==")
        h_tot, regions, regions_h, proved_exact, edges_removed = None, None, None, False, None
        partition_time = None
        if method == 'mdd':
            vertices_list = self.vertices.values.tolist()
            if type(vertices_list[0]) != list:
                vertices_list = [[val] for val in vertices_list]
            neighbors_list = [adj for adj in self.neighbors.values()]
            t1 = time.time()
            h_tot, proved_exact, edges_removed = solve_regionalization(vertices_list, neighbors_list, self.edges, k, W, cutoff)
            partition_time = time.time() - t1
            self.times['mdd_partition'] = partition_time
            regions, regions_h = self.del_edges_2_regions(edges_removed)
        elif method == 'redcap':
            t1 = time.time()
            h_tot, regions, regions_h, edges_removed = self.redcap(k)
            partition_time = time.time() - t1
            self.times['redcap_partition'] = partition_time
        if self.talk:
            print("h_tot  {}".format(h_tot))
            print("time {} sec".format(partition_time))
        return h_tot, regions, regions_h, proved_exact, edges_removed, partition_time

    def redcap(self,k):
        edges = {}
        for edge in self.edges:
            edges[edge] = True
        regions = [list(self.vertices.index)]
        edges_removed = []
        H = [self.compute_h(list(self.vertices.index))]
        while len(regions) < k:
            best_gain = 0.0
            best_edge = None
            region_cut = None
            new_regions = None
            new_h = None
            for e,v in edges.items():
                if v:
                    edges[e] = False
                    r1 = self.dfs_connected_vertex(e[0],edges)
                    h1 = self.compute_h(r1)
                    r2 = self.dfs_connected_vertex(e[1], edges)
                    h2 = self.compute_h(r2)
                    for i,region in enumerate(regions):
                        if e[0] in region and e[1] in region:
                            gain = H[i] - h1 - h2
                            if gain > best_gain:
                                best_gain = gain
                                best_edge = e
                                region_cut = i
                                new_regions = [r1,r2]
                                new_h = [h1,h2]
                    edges[e] = True
            updated_regions = []
            updated_h = []
            edges[best_edge] = False
            edges_removed.append(best_edge)
            for i in range(len(regions)):
                if i == region_cut:
                    updated_regions += new_regions
                    updated_h += new_h
                else:
                    updated_regions.append(regions[i])
                    updated_h.append(H[i])
            regions = updated_regions.copy()
            H = updated_h.copy()
        h_tot = sum(H)
        return h_tot, regions, H, edges_removed

    def del_edges_2_regions(self,del_edges):
        regions = []
        regions_h = []
        edges = {edge: (edge not in del_edges) for edge in self.edges}
        visited = []
        for v in self.vertices.index:
            if v not in visited:
                region = self.dfs_connected_vertex(v,edges)
                visited += region
                regions.append(region)
                regions_h.append(self.compute_h(region))
        return regions, regions_h

    def to_file(self):
        path = './data/'+self.name+'/'+self.name+'_sct.csv'
        if self.method == 'MST':
            path = './data/'+self.name+'/'+self.name+'_mst.csv'
        with open(path,'w') as f:
            for i,edge in enumerate(self.edges):
                f.write(str(edge[0])+','+str(edge[1]))
                if i < len(self.edges) -1:
                    f.write(' ')
            f.write('\n')
            for i,n in self.neighbors.items():
                for j,v in enumerate(n):
                    f.write(str(v))
                    if j < len(n) -1:
                        f.write(' ')
                if i < len(self.neighbors) -1:
                    f.write('\n')

    def read_file(self):
        path = './data/' + self.name + '/' + self.name + '_sct.csv'
        if self.method == 'MST':
            path = './data/' + self.name + '/' + self.name + '_mst.csv'
        edges = []
        neighbors = {v : [] for v in self.vertices.index}
        with open(path) as f:
            lines = f.readlines()
            es = lines[0].split(' ')
            for edge in es:
                v = edge.split(',')
                edges.append((int(v[0]),int(v[1])))
            for i,n in enumerate(lines[1:]):
                for v in n.split(' '):
                    neighbors[i].append(int(v))
        return edges, neighbors



class Regionalization_result:
    def __init__(self, h_tot, regions, regions_h, proved_exact, partition_time):
        self.global_heterogeneity = h_tot
        self.regions = regions
        self.regions_heterogeneity = regions_h
        self.exact_solution = proved_exact
        self.partition_time = partition_time
