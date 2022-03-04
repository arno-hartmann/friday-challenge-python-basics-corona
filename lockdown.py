
def calculateLockdown(data, limit):
    actives = data[-1]['Active'] - data[-7]['Active']
    print("actives in bb: ",actives)
    if actives >= limit:
        print("lockdown")
        lockdown = True
    else:
        print("no lockdown")
        lockdown = False

    return lockdown