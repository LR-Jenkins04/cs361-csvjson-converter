# cs361-csvjson-converter
Program Setup:
to set the program up, you simply need to set up the API call locations (url/etc) that are in the code. What needs to be filled out is clearly marked in the code itself. 

Program interaction:
the program only waits to be told to execute by the main program (an example of which is provided as main.py). No real data is transferred between programs, but data is fetched from the rest api that is provided and converted to/from a file.

Program execution:
to execute the program, first make sure that the converter programs are running in the backgorund, and then run either a main.py program or any other program that connects through a ZMQ pipe and sends any data (what the data is doesn't matter, it just waits to receive anything)

UML diagram :
'go' signal sent -> program requests database data -> database sends data -> program receives data -> program modifies and saves data
(or in the reverse order)
