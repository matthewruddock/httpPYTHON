"""
   client:
"""

import time
import socket

HOST = '127.0.0.1'  # connect to the local host
PORT = 12345        # connect to this port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))         # connect to the server
    s.sendall(b'Hello world')       # send some data to the server

    data = s.recv(1024)      # recv data
    print('From server: ' + repr(data))
    time.sleep(5)
    ## could continue communication
    ## OR 
    ## look for a delimiter