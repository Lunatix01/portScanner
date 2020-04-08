#!/bin/python3
import sys
import socket
if len(sys.argv)==2:
    target= sys.argv[1]
else: 
    print("please enter your IP Address")
    print("syntax: python3 sock.py <ip>")
    sys.exit()
print("+" * 60)
print("scanning...")
print("+" * 60)
count = 0
try:
    for port in range(1,65535):
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           socket.setdefaulttimeout(1)
           result= s.connect_ex((target,port))
           if result ==0:
             print("{} is open".format(port))
             count+=1
           s.close()

except KeyboardInterrupt:
	print("closing")
except socket.gaierror:
    print(" Host is not resolved")
    sys.exit()
except socket.error:
    print("cannot connect to this ip")
    sys.exit()        	
print("+" * 60)
if count>1:	
   print("{} ports are open".format(count))	
else:
   print("{} port is open".format(count))	