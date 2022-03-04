
def calculateTrend(data):
    thisWeekActives = data[-1]['Active'] - data[-7]['Active']
    lastWeekActives = data[-8]['Active'] - data[-15]['Active']
    
    if thisWeekActives == lastWeekActives:
        print("same, same, but different")
        trend = "CONSTANT"
    elif thisWeekActives <= lastWeekActives: 
        print ("lower")
        trend = "DOWN"
    else:
        print("higher")
        trend = "UP"

    return trend