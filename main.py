#program to signal other programs to activate
import zmq
context = zmq.Context()

#talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.send(b"1")
print("program executed")
