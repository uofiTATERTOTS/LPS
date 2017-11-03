"""
server2.py
Simple UDP/IP socket server on port 3000. Takes IP address of local device as an argument
ex run "python server1.py [ip_addr]"
UDP is connectionless - just send/receive packets (datagrams) 
"""
import socket
import sys

# create socket object using the UDP INET protocol
# would change AF_INET and SOCK_DGRAM ultimately (to something lower level)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = str(sys.argv[1]) # set host to given ip address, may be able to use 'localhost'
port = 3000
# bind socket to given ip addr and port
s.bind((host, port))

while True:
    # receives 1 bytes from client
    data1, addr = s.recvfrom(1)
    # send 1 byte message in response receive another message
    # and print received message
    s.sendto(b"1", addr)
    data2, addr = s.recvfrom(1)
    print(data1)
    print(data2)
