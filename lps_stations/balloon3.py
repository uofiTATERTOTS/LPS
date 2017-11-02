# Python 3

import socket
import lps

# create socket objects
balloon3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
balloon3.bind(lps.b3)

# initialize - respond to query from base
init_g, addr_g = balloon3.recvfrom(4)
if init_g == b'Who?':
	balloon3.sendto(b'3', lps.g)
	print("Ready\n")
	
for i in range(0, lps.trials):
	# Reference locating sequence
	s5, addr5 = balloon3.recvfrom(1)
	print('Received ', s5)
	balloon3.sendto(lps.s6, lps.g)
	print('Sent ', lps.s6)

	balloon3.sendto(lps.s7, lps.b2)
	print('Sent ', lps.s7)
	s8, addr8 = balloon3.recvfrom(1)
	print('Received ', s8)

	s11, addr11 = balloon3.recvfrom(1)
	print('Received ', s11)
	balloon3.sendto(lps.s12, lps.b1)
	print('Sent ', lps.s12)

	# Tag locating sequence
	sgo, addrgo = balloon3.recvfrom(2)
	print('Received "go" from tag')
	balloon3.sendto(lps.s17, lps.t1)
	print('Sent ', lps.s17)
	s18, addr18 = balloon3.recvfrom(1)
	print('Received ', s18)
	
	# tell base sequence done so may repeat
	balloon3.sendto(b'done', lps.g)
	print('\n')
	

