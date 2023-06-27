## BLS & BEA - Python Database API Connection

This repository contains Python files that facilitate the extraction of data from the BLS (Bureau of Labor Statistics) and BEA (Bureau of Economic Analysis) databases using their respective APIs. The provided Python scripts allow you to establish a connection with the databases and retrieve the desired data for further analysis or processing.

### Prerequisites

Required Python libraries: 'requests', 'json', 'pandas'

### BLS API Connection
The BLSdata file provides a Python function BLSData that connect to the BLS database using its API. It provides methods to authenticate, query data, and retrieve the results in a structured format.

To use the BLS API, follow these steps:

1. Obtain your BLS API key from the BLS API Registration page. In the file, copy your API key to the variable bls_key as default.
2. Go to [BLS website](https://beta.bls.gov/dataQuery/search) to find the Series ID.
3. Implement your desired data query by adding seriesID, startYr and endYr in the BLSdata function.
4. Run the bls_api.py file to execute your query and retrieve the data from the BLS database.

### BEA API Connection
The BEAdata file provides a Python function BEAData that enables connecting to the BEA database using its API. It offers methods to authenticate, query data, and obtain the results in a structured format.

To utilize the BEA API, follow these steps:

1. Obtain your BEA API key from the BEA Data API page. In the file, copy your API key to the variable api_key as default.
2. Go to [BEA NIPA Tables](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey) to find the table name.
3. Implement your desired data query by adding tablename, frequency and year in the BEAdata function.
4. Execute your query and retrieve the data from the BEA database.

### Example Usage
The repository includes example usages of both the BLS and BEA API connections in the example_usage.py file. You can refer to this file to understand how to retrieve data from the respective databases.
