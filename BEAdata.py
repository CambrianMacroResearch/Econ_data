import pandas as pd
import requests
import json


def BEAdata(name, frequency, year, api_key='Add Your Key Here'):

    url = f'https://apps.bea.gov/api/data/?UserID={api_key}' \
          f'&method=GetData' \
          f'&DataSetName=NIPA' \
          f'&TableName={name}' \
          f'&Frequency={frequency}' \
          f'&Year={year}' \
          f'&ResultFormat=JSON'

    response = requests.get(url)
    json_data = json.loads(response.text)

    # Convert data to dataframe
    df = pd.json_normalize(json_data['BEAAPI']['Results']['Data'])
    df_filtered = df[['LineNumber', 'LineDescription', 'TimePeriod', 'DataValue']].copy()

    # Convert the value to numbers
    df_filtered['DataValue'] = pd.to_numeric(df_filtered['DataValue'], errors='coerce')

    # Convert TimePeriod column into Date column
    if frequency == 'M':
        df_filtered['Date'] = pd.to_datetime(df_filtered['TimePeriod'].str[0:4]
                                             + '-' + df_filtered['TimePeriod'].str[5:], format='%Y-%m')
    else:
        df_filtered['Date'] = df_filtered['TimePeriod']

    return df_filtered