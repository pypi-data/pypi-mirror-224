import pandas as pd
import requests
from io import StringIO
from tabulate import tabulate

def dataset(key='csv'):
    try:
        url = "https://raw.githubusercontent.com/DATAisENOUGH/datasets_fetcher/main/data.csv"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
        req = requests.get(url, headers=headers)
        data1 = StringIO(req.text)
        data = pd.read_csv(data1)
        originaldata = data

        url2 = data.loc[data['DATASET-ID'] == key, 'DATASET-URL'].iloc[0]
        req = requests.get(url2, headers=headers)
        data1 = StringIO(req.text)
        data = pd.read_csv(data1)
        originaldata = data

        return data
    except Exception:
        print(tabulate(data, headers='keys', tablefmt='grid'))
        return print('''
    import datafetcher
    # print(datafetcher.dataset('datset_name'))
    print(datafetcher.dataset('AustralianElections'))

# Explore my GitHub profile for innovative projects and career growth ideas.
    https://github.com/dataisenough
''')