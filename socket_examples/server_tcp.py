"""
server1.py
Simple TCP/IP socket server on port 3000. Takes IP address of local device as an argument
ex run "python server1.py [ip_addr]"
Purpose of server socket is just to create client sockets in response to connection requests
"""
import socket
import sys

# create socket object using the TCP INET protocol
# would change AF_INET and SOCK_STREAM ultimately (to something lower level)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = str(sys.argv[1]) # set host to given ip address, may be able to use 'localhost'
port = 3000
# bind socket to given ip addr and port
s.bind((host, port))

s.listen(1) # listen, queue up to 1 connect request
while True:
    # creates client socket "c" to talk to connected device
    c, addr = s.accept()
    print("Got connection from",addr)
    c.send(b"connected")
    c.close()
