# Python 3

import socket
import lps

# create socket objects
tag1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tag1.bind(lps.t1)

# initialize - respond to query from base
init_g, addr_g = tag1.recvfrom(4)
if init_g == b'Who?':
	tag1.sendto(b'4', lps.g)
	print("Ready\n")
	
for i in range(0, lps.trials):
	# tag locating sequence, need to figure out multicasting
	s13, addr13 = tag1.recvfrom(1)
	print('Received ', s13)
	tag1.sendto(lps.s14, lps.b1)
	print('Sent ', lps.s14)
	
	tag1.sendto(b'go', lps.b2)
	print('sent "go" to balloon2')
	s15, addr15 = tag1.recvfrom(1)
	print('Received ', s15)
	tag1.sendto(lps.s16, lps.b2)
	print('Sent ', lps.s16)
	
	tag1.sendto(b'go', lps.b3)
	print('sent "go" to balloon3')
	s17, addr17 = tag1.recvfrom(1)
	print('Received ', s17)
	tag1.sendto(lps.s18, lps.b3)
	print('Sent ', lps.s18)
	
	print('\n')
