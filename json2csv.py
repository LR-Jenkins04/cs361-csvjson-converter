#import necessary libraries
#note that you may need to install these on your local machine
import json
import csv
import requests
import zmq

"""
FOR DEBUGGING IN IMPLEMENTATION
I am inexperienced with rest API's, and have used them very little
I also do not have a url with which to properly test this implementation

if it needs modificaiton, as long as this program eventually has a json
object stored under the name book_data the program should work.
"""


input_url = "PUT YOUR URL HERE"
output_file = "PUT YOUR OUTPUT FILENAME HERE"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def main():
    #wait for signal from main program
    wait = socket.recv()

    #rest API request goes here
    response = requests.get(input_url)#make request
    book_data = json.load(response) #load into json format 
    

    #(used for testing, commented out for final) open local file as json
    #with open('test.json') as json_file:
    #    book_data = json.load(json_file)

    #open csv file 
    #put the name of the file you want produced here
    #note that the file will be erased and filled with entirely new contents
    book_file = open(output_file, 'w')
    
    #initialize csv writer
    csv_writer = csv.writer(book_file)

    #write to csv file
    count = 0   #flag to count number of lines to print headers
    for book in book_data:
        if count == 0:
            #write header to csv if first row
            header = book.keys()
            csv_writer.writerow(header)
            count += 1
        #write a row of csv data
        csv_writer.writerow(book.values())
    book_file.close()



#execute main function
if __name__ == "__main__":
    main();

