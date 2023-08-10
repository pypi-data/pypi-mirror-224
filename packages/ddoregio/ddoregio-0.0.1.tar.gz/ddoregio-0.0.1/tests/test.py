from regiotool import partitioning

if __name__ == '__main__':
    zones = pd.read_pickle('../tests/ecodemo_NUTS1.pkl')
    attributes = ['density', 'gdp_inhabitant', 'median_age', 'rate_migration']
    result = partitioning(5, zones, attributes)
    print(result.global_heterogeneity)
    print(result.regions)
