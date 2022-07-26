from io import BytesIO
from operator import index
import zipfile,requests
import json, urllib.request
import csv
import io 
import urllib 
import sys

import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mlp_dates
import time




URL = "https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip"

#wget.download(URL)

req = requests.get(URL)

#this will extract file
zip_file = zipfile.ZipFile(BytesIO(req.content))
zip_file.extractall("data_file")



#parsing from file

with open("data_file/jodi_gas_beta.csv","r") as f: 
    data = {}
    reader = csv.reader(f)

    #here I made same data structure like in an example

    data = {"series_id":"",
    "points":[],
    "fields":{}}
    next(reader)

    

    #I choose REF_AREA, TIME_PERIOD, ENERGY_PRODUCT and FLOW_BREAKDOWN as relevant for this data extraction

    for row in reader:

        #reader = pd.read_csv("data_file/jodi_gas_beta.csv")
        #reader[row[1]] = pd.to_datetime(row[1])
        
        #date = reader.sort_values(by="TIME_PERIOD")
        data["series_id"] = row[0]
        data["points"] = [row[1],row[5]]
        data["fields"] = {row[2]:row[3]}

        json_object = json.dumps(data, indent= 4)
        print(json_object)
        sys.stdout.write('\n')











