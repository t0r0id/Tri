import json
import requests
import numpy as np

url='https://maps.googleapis.com/maps/api/distancematrix/json'

params = dict(
    origins='Hostel 6, Indian Institute of Technology Bombay, Main Gate Path, Students Residential Zone, IIT Area, Powai, Mumbai, Maharashtra 400076, India|18.922367,72.833698',
    destinations='Hostel 6, Indian Institute of Technology Bombay, Main Gate Path, Students Residential Zone, IIT Area, Powai, Mumbai, Maharashtra 400076, India|18.922367,72.833698',
    key='AIzaSyAkyOPwCARgHCb5b7LK8XbWprn06HCXAzg'
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

distances=np.zeros((2,2),dtype=int)
durations=np.zeros((2,2),dtype=float)

for i in range(2):
    for j in range(2):
        distances[i][j]=data['rows'][i]['elements'][j]['distance']['value']/1000
        durations[i][j]=data['rows'][i]['elements'][j]['duration']['value']/60

print durations
print distances
