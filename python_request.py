import requests
from writeJSON import writeJSONFile
import trend
import lockdown
import active
import cases



#Aufgabe: 
lockdown_limiter = 1000

url = requests.get("https://api.covid19api.com/live/country/barbados/status/confirmed")

#response is an array of dicts
response = url.json()


print(cases, active)

print(trend.calculateTrend(response))

print(lockdown.calculateLockdown(response, lockdown_limiter))

print(active.get_active(response))
print(cases.get_cases(response))