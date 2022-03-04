import requests
from writeJSON import writeJSONFile

#Aufgabe: 


url = requests.get("https://api.covid19api.com/live/country/switzerland/status/confirmed")

#response is an array of dicts
response = url.json()

# x = (len(response))-1
# y = response[-7]

cases = response[-1]['Confirmed'] - response[-8]['Confirmed']
active = response[-1]['Active'] - response[-8]['Active']

print(cases, active)
