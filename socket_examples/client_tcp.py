"""
client1.py
Simple TCP/IP socket client. Connects to server at IP address given as an argumee
nt
ex run "python client1.py [ip_addr]" and assumes server listening on port 3000
"""
import socket
import sys

# create socket object using TCP INET protocol
# would change AF_INET and SOCK_STREAM ultimately to lower level
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = str(sys.argv[1]) # set host to given ip address (of server)
port = 3000 # server port

# connect to server
s.connect((host, port))

# receive 9 bytes and print, then close connection
print(s.recv(9))
s.close()
