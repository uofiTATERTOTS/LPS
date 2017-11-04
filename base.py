'''
```
'''
import socket
import time
import numpy as np
import netifaces
from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt

def positioning_sequence_base(address, port):
    timeout = 10

    program_start = time.time()

    print address

    base = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    base.bind((address, port))
    base.settimeout(1)

    responses = list()
    nodes = list()
    node_index = 0

    start = time.time()
    end = start + timeout
    while time.time() < end:
        try:
            new_response, new_address = base.recvfrom(1024)
        except:
            pass
        else:
            responses.append(new_response)
            nodes.append(new_address)
            print "Received", new_response, "from", new_address
            print "Sending", node_index, "to", new_address
            base.sendto(str(node_index), new_address)
            node_index = node_index + 1

    print "Initialization complete, ready to begin."
    print "Number of nodes: ", len(nodes)

    for ii in range(len(nodes)):
        base.sendto('ready', nodes[ii])

    for ii in range(len(nodes)):
        for kk in range(len(nodes)):
            print "Sending "+str(kk)+","+str(nodes[kk][0])+","+str(nodes[kk][1])
            base.sendto(str(kk)+","+str(nodes[kk][0])+","+str(nodes[kk][1]), nodes[ii])
        base.sendto('done', nodes[ii])
        try:
            new_response, new_address = base.recvfrom(1)
        except:
            pass
        else: 
            if new_response == "0":
                pass
            else:
                print "Initialization error."
                break

    peak_1 = 0
    peak_2 = 1        
    flag = 1
    time_end = time.time() + 100
    threshold = 0.1
    n = 1000
    flight_times_1 = np.zeros((n,len(nodes)))
    flight_times_2 = np.zeros((n,len(nodes)))
    
    if len(nodes) != 0:
        for ii in range(len(nodes)):
            peak_1 = 0
            peak_2 = 1
            iterations = 0
            flight_times_1_filt = list()
            flight_times_2_filt = list()
            start = time.time()
            end = start + 10
            print "\nNode ", ii
            while abs(peak_1 - peak_2) > threshold:
                for kk in range(n):
                    if abs(peak_1 - peak_2) < threshold:
                        print "Converged"
                        break
                    if time.time() > time_end:
                        print "Timed out in second loop"
                        break
                    start = time.time()
                    base.sendto(str(ii), nodes[ii])
                    while time.time() < end:
                        try:
                            new_response, new_address = base.recvfrom(1)
                        except:
                            pass
                        else:
                            iterations = iterations + 1
                            if iterations % 100 == 0:
                                print iterations, '\r',
                            if flag == 1:
                                flight_times_1[kk][ii] = time.time()-start
                                flag = 2
                            elif flag == 2:
                                flight_times_2[kk][ii] = time.time()-start
                                flag = 1
                            break

                if len(flight_times_1) > 0 and len(flight_times_1[0][:]) > 0:
                    for mm in range(len(flight_times_1)):
                        if flight_times_1[mm][ii] != 0.0:
                            flight_times_1_filt.append(flight_times_1[mm][ii])
                    if len(flight_times_1_filt) > 0:
                        kde_1 = gaussian_kde(flight_times_1_filt, 0.05)
                        dist_space_1 = np.linspace(0, max(flight_times_1_filt), n)
                        values_1 = np.zeros(len(dist_space_1))
                        maximum_1 = 0
                        index_1 = 0

                if len(flight_times_2) > 0 and len(flight_times_2[0][:]) > 0:
                    for mm in range(len(flight_times_2)):
                        if flight_times_2[mm][ii] != 0.0:
                            flight_times_2_filt.append(flight_times_2[mm][ii])
                    if len(flight_times_2_filt) > 0:
                        kde_2 = gaussian_kde(flight_times_2_filt, 0.05)
                        dist_space_2 = np.linspace(0, max(flight_times_2_filt), n)
                        values_2 = np.zeros(len(dist_space_2))
                        maximum_2 = 0
                        index_2 = 0
                if 'dist_space_1' in locals():
                    for mm in range(len(dist_space_1)):
                        values_1[mm] = kde_1(dist_space_1[mm])
                        if values_1[mm] > maximum_1:
                            maximum_1 = values_1[mm]
                            index_1 = mm
                    peak_1 = dist_space_1[index_1]
                    for mm in range(len(dist_space_2)):
                        values_2[mm] = kde_2(dist_space_2[mm])
                        if values_2[mm] > maximum_2:
                            maximum_2 = values_2[mm]
                            index_2 = mm
                    peak_2 = dist_space_2[index_2]
            if 'dist_space_1' in locals() and abs(peak_1 - peak_2) < threshold:
                print "Converged"
                plt.plot(dist_space_1, kde_1(dist_space_1))
                plt.show()
                plt.plot(dist_space_2, kde_2(dist_space_2))
                plt.show()
                print iterations, "iterations"
                print "Node", ii, "Peak 1:", peak_1
                print "Node", ii, "Peak 2:", peak_2
            if abs(peak_1 - peak_2) > threshold: 
                print "Failed to converge"

        with open("flight_times_1.txt", 'w') as fp:
            for ii in range(len(flight_times_1)):
                for kk in range(len(flight_times_1[0][:])):
                    fp.write('{0:1.12f}'.format(flight_times_1[ii][kk])+'\t')
                fp.write('\n')
        with open("flight_times_2.txt", 'w') as fp:
            for ii in range(len(flight_times_2)):
                for kk in range(len(flight_times_2[0][:])):
                    fp.write('{0:1.12f}'.format(flight_times_2[ii][kk])+'\t')
                fp.write('\n')

    if len(nodes) > 0:
        base.sendto('begin', nodes[0])
        print "Sending Begin"
    else:
        print "Failed to begin. Zero nodes connected"

    if len(nodes) > 0:
        start = time.time()
        end = start + 5
        while time.time() < end:
            try:
                new_response, new_address = base.recvfrom(1024)
            except:
                pass
            else:
                if new_response == "complete":
                    print "Received Complete"
                    break 

    print "Complete"
    print '{0:1.12f}'.format(time.time() - program_start), "seconds elapsed"
    
positioning_sequence_base('192.168.137.1', 3010)

'''
```
''' ;