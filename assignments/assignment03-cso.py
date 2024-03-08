# Assignment 03
# Write a program that retrieves the dataset for the "Exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json"
# Author: Tanja Juric

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# retrieving data from CSO 
def getData():
    response = requests.get(url)
    return response.json()

# saving data into a file in json format
if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getData()), file=fp)