#import dependancies (you may need to install them on your machine
import csv
import json
import requests
import zmq

"""
note that I am inexperienced with rest API's and lack a 
database to test with, as such this may not be functional code.
the code above is all funcitonal, and json_data is a valid json
file of the csv information, so fixing the api shoudln't be hard
"""

#api definitions, fill with your database info
API_POINT = "YOUR LINK HERE"
API_KEY = "YOUR KEY HERE"


inFile = "YOUR FILE NAME HERE"
#output file, only needed for testing
#outFile = "output.json"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def main():
    #wait for go signal from main
    wait = socket.recv()

    #open and convert csv file
    with open(inFile, encoding = 'utf-8') as csvfile:
        csvReader = csv.DictReader(csvfile)
        data = list(csvReader)

    json_data = json.dumps(data, indent = 4)

    #output json data to local file (used for testing)
    #with open(outFile, 'w', encoding = 'utf-8') as jsonfile:
    #    jsonfile.write(json_data)

    #send json information over rest API
    r = requests.post(url = API_POINT, data = data)    



if __name__ == "__main__":
    main()
