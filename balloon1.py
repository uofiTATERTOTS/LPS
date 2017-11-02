# Python 3

import socket
import lps

# create socket objects
balloon1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
balloon1.bind(lps.b1)

# initialize - respond to query from base
init_g, addr_g = balloon1.recvfrom(4)
if init_g == b'Who?':
	balloon1.sendto(b'1', lps.g)
	print("Ready\n")

for i in range(0, lps.trials):
	# Reference locating sequence
	s1, addr1 = balloon1.recvfrom(1)
	print('Received ', s1)
	balloon1.sendto(lps.s2, lps.g)
	print('Sent ', lps.s2)

	s9, addr9 = balloon1.recvfrom(1)
	print('Received ', s9)
	balloon1.sendto(lps.s10, lps.b2)
	print('Sent ', lps.s10)

	balloon1.sendto(lps.s11, lps.b3)
	print('Sent ', lps.s11)
	s12, addr12 = balloon1.recvfrom(1)
	print('Received ', s12)

	# Tag locating sequence - figure out multicasting
	balloon1.sendto(lps.s13, lps.t1)
	print('Sent ', lps.s13)
	s14, addr14 = balloon1.recvfrom(1)
	print('Received ', s14)
	print('\n')

