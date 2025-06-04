#sarah verburg 06-04

import json
import urllib.request

#get data from downloaded file
json_data = 'temperature_anomaly.json'

#get data from URL
#json_data = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json"

with open(json_data, encoding='utf-8') as data:
# with urllib.request.urlopen(json_data) as json_stream:
#     data = json_stream.read().decode('utf-8')
    anomalies = json.load(data) #.loads() to get from stream/url

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(year, "...", value)

print("-"*40)

print(anomalies['citation'])
