
def calculateLockdown(data, limit):
    actives = data[-1]['Active'] - data[-7]['Active']
    if actives >= limit:
        lockdown = True
    else:
        lockdown = False
    return lockdown