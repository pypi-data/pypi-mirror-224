from regiotool import partitioning
import pandas as pd

if __name__ == '__main__':
    zones = pd.read_pickle('../../tests/ecodemo_NUTS1.pkl')
    attributes = ['density', 'gdp_inhabitant', 'median_age', 'rate_migration']
    result = partitioning(3, zones, attributes)
    print(result.global_heterogeneity)
    print(result.regions)
