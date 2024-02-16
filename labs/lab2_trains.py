# Tanja Juric
# Lab 2 
# Write a programme that prints all the trains to the console - only trains that have a train code that starts with D

# reads XML from URL and prints it out
from xml.dom.minidom import parseString
import requests
import csv

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

# print (doc.toprettyxml(newl=''))

# use with so the file is properly closed after writing
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

# https://docs.python.org/3/library/xml.dom.html
# print each traincode
    
# store into csv
with  open('trains_with_D.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        # traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        # traincode = traincodenode.firstChild.nodeValue.strip()
        # print (traincode)
        
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            train_code = datanode.firstChild.nodeValue.strip()
            if retrieveTag == "TrainCode" and train_code[0] == "D":
                dataList.append(train_code)


        train_writer.writerow(dataList)
        
        # dataList = []
        # dataList.append(traincode)
        # train_writer.writerow(dataList)

# print latitudes
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlatitude = trainlatitudenode.firstChild.nodeValue.strip()
    print (trainlatitude)


       