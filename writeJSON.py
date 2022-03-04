import json

def writeJSONFile(data):
    with open("corona-data.json",'r+') as File:
        File.write(data)
