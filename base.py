# Python 3

import socket
import lps
# should use received address for clarity? after recvfrom

# create socket objects
base = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
base.bind(lps.g)

#base.settimeout(
#base.setblocking(0)

# initialize - wait for all units online
# needs work, should loop until get a response
base.sendto(b'Who?', lps.b1)
reply_b1, addr_b1 = base.recvfrom(1)
if int(reply_b1) == 1:
	print('Balloon 1 is ready')

base.sendto(b'Who?', lps.b2)
reply_b2, addr_b2 = base.recvfrom(1)
if int(reply_b2) == 2:
	print('Balloon 2 is ready')
	
base.sendto(b'Who?', lps.b3)
reply_b3, addr_b3 = base.recvfrom(1)
if int(reply_b3) == 3:
	print('Balloon 3 is ready\n')	
	
base.sendto(b'Who?', lps.t1)
reply_t1, addr_t1 = base.recvfrom(1)
if int(reply_t1) == 4:
	print('Tag 1 is ready\n')	

for i in range(0, lps.trials):
	# Reference locating sequence
	base.sendto(lps.s1, lps.b1)
	print('Sent ', lps.s1)
	s2, addr2 = base.recvfrom(1) # can just use recv, keep recvfrom for debugging
	print('Received ', s2)

	base.sendto(lps.s3, lps.b2)
	print('Sent ', lps.s3)
	s4, addr4 = base.recvfrom(1)
	print('Recieved ', s4)

	base.sendto(lps.s5, lps.b3)
	print('Sent ', lps.s5)
	s6, addr6 = base.recvfrom(1)
	print('Received ', s6)
	
	# wait until full sequence finished to loop
	sdone, addrdone = base.recvfrom(4)
	print('Received ', sdone)
	print('\n')
