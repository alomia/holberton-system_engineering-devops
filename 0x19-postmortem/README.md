# Nginx server error

### ISSUE SUMMARY

On Thursday February 17, 2021 we could see that one of our web servers was not receiving all HTTP requests, after debugging and investigating we could realize that the problem was the configuration of the ulimit package in ubuntu, this had a low configuration that affected the requests.



### **DETAILED DESCRIPTION OF IMPACT**

The main problem with this was that when this server rejected the requests the operations were performed on the other servers, this added to the amount of requests made, slowed down the connection and the responses to the clients.



### TIMELINE

February 17–2:30 p.m: we realize that one of our servers is not accepting all HTTP requests made to it.

February 17–2:57 p.m: A test was performed to simulate the sending of HTTP requests to the servers, using ApacheBench, with this we could observe that one of the servers is rejecting most of these requests.

February 17–3:15 p.m: Once these tests were done we decided to look at the configuration of Nginx, we realized that there was a limit on the number of open file descriptors per process, when testing we realized that if there were files that were processed but not all, which tells us of a limit.

February 17–3:20 p.m: We check the descriptor limit, When we did this we realized that the ULIMIT was at 15, which is a bit low for the amount of requests expected for this server, so we increased this number.

February 17–3:23 p.m: The server was restarted and all tests were run again. At this point all tests passed.



### ROOT CAUSE AND RESOLUTION

The cause of all this problem was an ULIMIT in the Nginx configuration file, as the number of files was a bit low, it could not process higher volumes of requests, so we increased the number so that this problem no longer existed.
For future similar problems we created a script to check all these processes automatically.



### CORRECTIVE AND PREVENTATIVE MEASURES

When new servers or configurations are added, everything must be tested to make sure they work and integrate correctly into the system.