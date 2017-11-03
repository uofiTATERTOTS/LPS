"""
client2.py
Simple UDP/IP socket client. Sends datagram to server at IP address
given as an argument
ex run "python client2.py [ip_addr]" and assumes server listening on port 3000
"""
import socket
import sys

trials = 10000

# create socket object using TCP INET protocol
# would change AF_INET and SOCK_STREAM ultimately to lower level?
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = str(sys.argv[1]) # set host to given ip address (of server)
port = 3000 # server port

for i in range(0, trials):
# send 2 byte message
	s.sendto(b"0", (host, port))

# receive and send another message, print 1 byte message
	data, addr = s.recvfrom(1)
	s.sendto(b"2", (host, port))

	print(data)
