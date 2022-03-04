
def calculateTrend(data):
    thisWeekActives = data[-1]['Active'] - data[-7]['Active']
    lastWeekActives = data[-8]['Active'] - data[-15]['Active']
    
    if thisWeekActives == lastWeekActives:
        trend = "CONSTANT"
    elif thisWeekActives <= lastWeekActives: 
        trend = "DOWN"
    else:
        trend = "UP"
    return trend