import json

def writeJSONFile(data):
    with open("corona-data.json",'a') as File:
        File.write(data)
        File.write('\n')
        File.close()
