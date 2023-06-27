import json
import requests
import pandas as pd


def getBLSdata(seriesID, startYr, endYr, bls_key='Add Your Key Here'):

    headers = {'Content-type': 'application/json'}
    # api url
    bls_api_url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

    # setup inputs to the api: series ID, start year, end year and api key
    data = json.dumps({"seriesid": [seriesID], "startyear": startYr, "endyear": endYr, "registrationKey": bls_key})

    # Initialize a list into which we will collect the data
    series_list = []

    # post to the api with inputs and get the output
    p = requests.post(bls_api_url, data=data, headers=headers)
    json_data = json.loads(p.text)

    # return print(json_data)

    # Parse the output into the list
    for series in json_data['Results']['series']:
        series_list = []
        seriesid = series['seriesID']
        for item in series['data']:
            year = item['year']
            period = item['period']
            value = item['value']

            if 'M01' <= period <= 'M12' or period <= 'A01':
                series_list.append([seriesid, year, period, value])

        return series_list


def BLSdata(seriesID, startYr, endYr):
    startYr = startYr
    seriesID = seriesID
    endYr = endYr
    data = getBLSdata(seriesID, startYr, endYr)
    # Convert list to DataFrame
    df = pd.DataFrame(data, columns=['ID', 'Year', 'Month', 'Value'])

    # Combine Year and Month columns into Date column
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].str[1:], format='%Y-%m')
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    return df