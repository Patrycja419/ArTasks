import pandas as pd
from pandas.util.testing import assert_frame_equal

from valuationService import ValuationService


def test():
    excepted =[]
    df_excepted = pd.DataFrame(excepted)
    tested_files = pd.DataFrame(ValuationService(r'csvFiles/test_files/data.csv', r'csvFiles/test_files/currencies.csv', r'csvFiles/test_files/matchings.csv').valuationLogic())
    df_excepted = pd.read_csv(r'test/top_products_excepted.csv')
    print(df_excepted)
    print(tested_files)
    df_tested_files = pd.DataFrame(tested_files)
    assert_frame_equal(df_tested_files, df_excepted)


test()
