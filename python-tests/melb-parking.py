# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 16:40:17 2019

@author: cjacobs1
"""

import json
import urllib

# Import the JSON data
def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
   
    # JSON data for Melbourne city
    parkingDataUrl = "https://data.melbourne.vic.gov.au/resource/vh2v-4nfs.json"
    jsonData = getResponse(parkingDataUrl)
    
    # Print the information stored for all locations with status=Unoccupied
    unoccupiedParks = [i for i in jsonData if i["status"] == "Unoccupied"]
    print(unoccupiedParks)
    
    # Write this information to JSON
    with open('data.txt', 'w') as outfile:
        json.dump(unoccupiedParks, outfile)
     
if __name__ == '__main__':
    main()