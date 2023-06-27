import BEAdata
import BLSdata


# Example: to extract CPI data from BLS

'''
CUSR0000SA0 : All items in U.S. city average, all urban consumers, seasonally adjusted
'''

df_CPI = BLSdata.BLSdata('CUSR0000SA0', 2019, 2023)
print(df_CPI)


# Example: To extract PCE data from BEA api

'''
T20804 : Table 2.8.4. Price Indexes for Personal Consumption Expenditures by Major Type of Product, Monthly
LineNumber
1 : Personal consumption expenditures (PCE)
2 : Goods
5 : Services
6 : Core PCE

'''

data_PCE = BEAdata.BEAdata('T20804', 'M', '2019, 2020, 2021, 2022, 2023')
df_PCE = data_PCE.loc[data_PCE['LineNumber'] == '1', ['Date', 'DataValue']]
df_corePCE = data_PCE.loc[data_PCE['LineNumber'] == '6', ['Date', 'DataValue']]
print(df_PCE)
print(df_corePCE)
