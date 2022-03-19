
"""
    Server
        - can only handle one conection at a time
"""

import socket                

#host = '127.0.0.1'    # listen on the local host only
#host = 'example.org'  # listen on IP that resolves to this host name
host = ''              # leave blank to listen on any IP or interface
port = 12345           # above 1023 are non-privileged, 1-65535
  
s = socket.socket()                 # open a socket
s.bind((host, port))                # bind to a host and port
s.listen(5)                        # start listening, optional (in Python py 3.5) backlog number for pending connections
print( "Listening on " + str(host) + ":" + str(port))

while True:                         # loop for connections ( one at a time )
    conn, addr = s.accept()         # block and wait for incoming connections
    print("Connection from " +  str(addr))
    while True:                     # loop to recv data
        data = conn.recv(1024)      # recv data
        if not data:                # no more data to recv (socket closed!!)
            break                   # break loop
        print("recv: " + str(data))
        conn.sendall(data)   # send data back
    print("Connection closed: " + str(addr))
    conn.close()                    # close connection