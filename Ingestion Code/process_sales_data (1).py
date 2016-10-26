__author__ = 'Will'

import pandas
import urllib.parse
import requests
from bs4 import BeautifulSoup


def zillow_hood_lookup(address):
    # encode the address to make it URL friendly for the Zillow API
    encoded_address = urllib.parse.quote(address)
    print(encoded_address)

    # lookup
    response = requests.get('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz1ffkz4wphjf_3fm17&address='+encoded_address+'&citystatezip=Washington%2C%20DC')

    # parse - example: <region id="121779" name="Riggs Park" type="neighborhood">
    response_bsObj = BeautifulSoup(response.text, "html.parser")
    hood = response_bsObj.find(name='region', attrs={'type':'neighborhood'})['name']

    return hood


df = pandas.read_csv('test.csv', sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None)


for index, row in df.iterrows():
    print(index)
    df.loc[index,'Neighborhood'] = zillow_hood_lookup(df.loc[index,'Address'])

print(df.info())



df.to_csv('output.csv')