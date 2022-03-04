import json

def writeJSONFile(data):
    with open("corona-data.json",'w') as File:
        File.write(data)
        File.close()
