import pandas as pd

class ValuationService:
    def __init__(self, df_data, df_currencies, df_matchings):
        self.df_data = pd.read_csv(df_data)
        self.df_currencies = pd.read_csv(df_currencies)
        self.df_matchings = pd.read_csv(df_matchings)

    def valuationLogic(self):

        dictData = {}
        for index, row in self.df_data.iterrows():
            matching_id = row.pop('matching_id')
            pricePLN = row['price'] * {row['currency']: row['ratio'] for index, row in self.df_currencies.iterrows()}[
                row['currency']]
            row['total_price_PLN'] = pricePLN * row['quantity']
            if matching_id not in dictData:
                dictData[matching_id] = []
            dictData[matching_id].append(row)

        for sortedElement in dictData.values():
            sortedElement = sorted(sortedElement, key=lambda row: row['total_price_PLN'], reverse=True)

        products = []
        for index, row in self.df_matchings.iterrows():
            matching_id = row['matching_id']
            sortedElement = dictData[row['matching_id']]
            elementLength = len(sortedElement)
            top_priced_cout = row['top_priced_cout']
            topLength = min(elementLength, top_priced_cout)
            topProducts = sortedElement[:topLength]
            total = sum(row['total_price_PLN'] for row in topProducts)
            products.append({
                'matching_id': matching_id,
                'total_price': total,
                'avg_price': total / topLength,
                'currency': 'PLN',
                'ignored_products_count': elementLength - topLength,
            })
            global df_products
            df_products = pd.DataFrame(products)

        return df_products

    def write_to_csv(self):
        df_products.to_csv('top_products.csv', index=False)


FilesValuationService = ValuationService(r'csvFiles/data.csv', r'csvFiles/currencies.csv', r'csvFiles/matchings.csv')
FilesValuationService.valuationLogic()
FilesValuationService.write_to_csv()

