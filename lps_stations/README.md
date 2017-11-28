<h1 align = center> LPS Stations </h1>
&emsp; &emsp; These files will carry out an 18 transmission sequence using datagrams. IP addresses must be set for each device in lps.py, which must be present in the same directory as each of the other files (for example balloon1.py needs lps.py available to run). The number of times the sequence will repeat can be also be set in lps.py, but there is no handling for failed transmissions and no built in timing. 
<br>
&emsp; &emsp; The transmission sequence is performed as follows:
&emsp; &emsp; &emsp; &emsp; 1   The base station (base.py) sends a signal to the first node (balloon1.py) 
&emsp; &emsp; &emsp; &emsp; 2   The first node replies
&emsp; &emsp; &emsp; &emsp; 3   The base station sends a signal to the second node (balloon2.py)
&emsp; &emsp; &emsp; &emsp; 4   The second node replies
&emsp; &emsp; &emsp; &emsp; 5   The base station sends a signal to the third node (balloon3.py)
&emsp; &emsp; &emsp; &emsp; 6   The third node replies
&emsp; &emsp; &emsp; &emsp; 7   The third node sends a signal to the second node
&emsp; &emsp; &emsp; &emsp; 8   The second node replies
&emsp; &emsp; &emsp; &emsp; 9   The second node sends a signal to the first node
&emsp; &emsp; &emsp; &emsp; 10  The first node replies
&emsp; &emsp; &emsp; &emsp; 12  The first node sends a signal to the tag
&emsp; &emsp; &emsp; &emsp; 13  The tag replies
&emsp; &emsp; &emsp; &emsp; 14  The second node sends a signal to the tag
&emsp; &emsp; &emsp; &emsp; 15  The tag replies
&emsp; &emsp; &emsp; &emsp; 16  The third node sends a signal to the tag
&emsp; &emsp; &emsp; &emsp; 17  The tag replies
&emsp; &emsp; &emsp; &emsp; 18  The first node sends a signal to the base station to signify the sequence is complete
