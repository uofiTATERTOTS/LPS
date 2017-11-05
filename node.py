'''
```
'''
import socket
import time

def positioning_sequence(base_address, base_port):
    start = time.time()
    end = start + 20

    node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    node.settimeout(1)
    base_address = (base_address, base_port)

    node.sendto("0", base_address)

    node_number = -1

    while time.time() < end:
        try:
            data, address = node.recvfrom(1024)
        except:
            pass
        else:
            print 'Base: \t', address[0]
            node_number = data.split(',')[0]
            data = ""
            break

    if node_number != -1:
        ready = False
        start = time.time()
        while ready == False:
            try:
                check = node.recv(5)
            except:
                pass
            else:
                if check == 'ready':
                    break
            if time.time() > start + 20:
                print "Timed out"
                break

        addresses = list()
        ports = list()
        while time.time() < start + 15:
            try:
                data, temp = node.recvfrom(1024)
            except:
                pass
            else:
                if data == "done":
                    node.sendto('0', base_address)
                    data = ''
                    break
                else:
                    addresses.append(data.split(',')[1])
                    ports.append(int(data.split(',')[2]))

        iterations = 0
        print_flag = False
        start = time.time()
        while time.time() < start + 100:
            try:
                data, address = node.recvfrom(10)
            except:
                pass
            else:
                if data == node_number:
                    if print_flag == False:
                        print "Sending", str(int(data)+1), "to", base_address[0]
                        print_flag = True
                    iterations = iterations + 1
                    print iterations, '\r',
                    node.sendto(str(int(data)+1), base_address)
                    data = ''
                elif data == "begin":
                    print iterations
                    print "Received Begin from", address, '\n'
                    data = ''
                    break
                else:
                    node.sendto('e', base_address)
                    print "Error in send/receive"
                    print data
                    data = ''
                    break

        flight_times = list()

        if len(addresses) > 1 and node_number == '0':
            for ii in range(len(addresses)-1):
                node.sendto('begin', (addresses[ii+1], ports[ii+1]))
                print "Sent Begin to", addresses[ii+1], ports[ii+1]

        
        complete = False
        flag_1 = 0
        start = time.time()
        while time.time() < start + 25:
            if complete == True:
                print "Completed secondary sequence"
                break
            if len(addresses) > 1:
                if node_number == '0':
                    start_time = time.time()
                    if flag_1 != 1:
                        print "Sent     n to  ", addresses[int(node_number)+1], ports[int(node_number)+1]
                        node.sendto('n', (addresses[int(node_number)+1], ports[int(node_number)+1]))
                        flag_1 = 1
                    try:
                        data, address = node.recvfrom(10)
                    except:
                        pass
                    else:
                        print "Received", data, "from", address[0], address[1]
                        if data == '0':
                            end_time = time.time()
                            flight_times.append(end_time-start_time)
                            data = ''
                        elif data == 'n':
                            data = ''
                            node.sendto('0', address)
                            print "Sent     0 to  ", address
                            complete = True
                        else:
                            print "Received", data, "expected '0' or 'n'"
                            print "Error. Quitting..."
                            data = ''
                            break
                elif node_number != '0':
                    try:
                        data, address = node.recvfrom(10)
                    except:
                        pass
                    else:
                        print "Received", data, "from", address[0], address[1]
                        if int(node_number) == len(addresses) - 1:
                            if data == 'n':
                                node.sendto('0', (addresses[int(node_number)-1], ports[int(node_number)-1]))
                                print "Sent     0 to  ", addresses[int(node_number)-1], ports[int(node_number)-1]
                                start_time = time.time()
                                node.sendto('n', (addresses[0], ports[0]))
                                node.sendto('complete', base_address)
                                print "Sent     n to  ", addresses[0], ports[0]
                                data = ''
                            elif data == '0':
                                end_time = time.time()
                                flight_times.append(end_time-start_time)
                                data = ''
                                complete = True
                            else:
                                print "Received", data, "expected 'n'"
                                print "Error. Quitting..."
                                data = ''
                                break
                        else:
                            if data == 'n':
                                data = ''
                                if int(node_number) > 0:
                                    node.sendto('0', (addresses[int(node_number)-1], ports[int(node_number)-1]))
                                    print "Sent     0 to  ", addresses[int(node_number)-1], ports[int(node_number)-1]
                                    start_time = time.time()
                                    node.sendto('n', (addresses[int(node_number)+1], ports[int(node_number)+1]))
                                    print "Sent     n to  ", addresses[int(node_number)+1], ports[int(node_number)+1]
                            elif data == '0':
                                end_time = time.time()
                                flight_times.append(end_time-start_time)
                                data = ''
                                complete = True
                            else:
                                print "Received", data, "expected '0' or 'n'"
                                print "Error. Quitting..."
                                data = ''
                                break
            else:
                print "Only one node active"
                break
    if 'iterations' in locals():
        print iterations, ' iterations.'
    
    if 'flight_times' in locals():
        for ii in range(len(flight_times)):
            node.sendto(node_number+','+str(flight_times[ii]), base_address)
    node.sendto(node_number+',complete', base_address)
        
    print "Complete"
    node.close()
    
positioning_sequence('192.168.137.1', 3010)
'''
```
'''; 