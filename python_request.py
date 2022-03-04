import requests
from writeJSON import writeJSONFile
import trend
#Aufgabe: 


url = requests.get("https://api.covid19api.com/live/country/barbados/status/confirmed")

#response is an array of dicts
response = url.json()

# x = (len(response))-1
# y = response[-7]

cases = response[-1]['Confirmed']
active = response[-1]['Active'] - response[-8]['Active']

print(cases, active)

print(trend.calculateTrend(response))
