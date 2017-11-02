# Python 3

import socket
import lps

# create socket objects
balloon2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
balloon2.bind(lps.b2)

# initialize - respond to query from base
init_g, addr_g = balloon2.recvfrom(4)
if init_g == b'Who?':
	balloon2.sendto(b'2', lps.g)
	print("Ready\n")
	
for i in range(0, lps.trials):
	# Reference locating sequence
	s3, addr3 = balloon2.recvfrom(1)
	print('Received ', s3)
	balloon2.sendto(lps.s4, lps.g)
	print('Sent ', lps.s4)

	s7, addr7 = balloon2.recvfrom(1)
	print('Received ', s7)
	balloon2.sendto(lps.s8, lps.b3)
	print('Sent ', lps.s8)

	balloon2.sendto(lps.s9, lps.b1)
	print('Sent ', lps.s9)
	s10, addr10 = balloon2.recvfrom(1)
	print('Received ', s10)

	# Tag locating sequence
	sgo, addrgo = balloon2.recvfrom(2)
	print('Received "go" from tag')
	balloon2.sendto(lps.s15, lps.t1)
	print('Sent ', lps.s15)
	s16, addr16 = balloon2.recvfrom(1)
	print('Received ', s16)
	print('\n')
	
	# figure out multicasting or something
