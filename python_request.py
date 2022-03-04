import requests
from writeJSON import writeJSONFile
import trend
import lockdown
import active
import cases
import json
import checkBuckets
import createBucket


lockdown_limiter = 1000

url = requests.get("https://api.covid19api.com/live/country/barbados/status/confirmed")

#response is an array of dicts
response = url.json()

cases = (cases.get_cases(response))
active = (active.get_active(response))
trend = (trend.calculateTrend(response))
lockdown = (lockdown.calculateLockdown(response, lockdown_limiter))

writeJSONFile((json.dumps({"cases": cases, "active": active, "trend": trend, "lockdown": lockdown})))

print(checkBuckets.checkforBuckets())
