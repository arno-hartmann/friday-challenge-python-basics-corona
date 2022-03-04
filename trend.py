
def calculateTrend(data):
    thisWeekActives = data[-1]['Active'] - data[-7]['Active']
    lastWeekActives = data[-8]['Active'] - data[-15]['Active']

    if thisWeekActives <= lastWeekActives:
        print ("lower")
    else:
        print("higher")