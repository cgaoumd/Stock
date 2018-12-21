#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:37:08 2018

@author: chao
"""

import urllib.request, urllib.parse, urllib.error
import json
import pandas as pd

# Request stock time series data from Alpha Vantage API
# Documentation can be found at https://www.alphavantage.co/documentation/#
serviceurl = 'https://www.alphavantage.co/query?'
srvfunc = 'TIME_SERIES_INTRADAY'
srvinterval = '1min'
srvoutputsz = 'full'
srvdatatype = 'json'
apikey = '5N4YTZZ9A71XLEV0'

while True:
    symbol = input('Enter symbol: ')
    if len(symbol) < 1: break

    url = serviceurl + 'function=' + srvfunc +'&symbol=' + symbol + '&interval=' \
    + srvinterval + '&outputsize=' + srvoutputsz + '&datatype=' + srvdatatype  \
    + '&apikey=' + apikey

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) # js should contain meta data and actual time series
    except:
        js = None

    if not js :
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    #print(json.dumps(js))
    keys = list(js.keys())
    dataframe = pd.DataFrame.from_dict(js[keys[1]], orient = 'index')
    dataframe = dataframe.astype(float)
    dataframe['1. open'].plot()