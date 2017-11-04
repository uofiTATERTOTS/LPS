<h1 align = "center"> Local Positioning </h1>
&emsp; &emsp; Finds the distance between nodes, using at least four reference nodes to find 
the position of a target node using multilateration by hyperboloids or three 
reference nodes to find the position using trilateration.
<br>
<br>
&emsp; &emsp; The <i> lps_stations </i> folder contains scripts for conducting the positioning sequence
using datagrams under the UDP protocol and without built in timing or time-out handling. 
in contrast to <i> base.py </i> and <i> node.py</i>, there is a different script for each
node (or balloon) and for the tag and base station, and the IP addresses and ports of each 
are explicitly set in <i> lps.py </i>. 
Note: These files are Python 3, while the other code is Python 2
