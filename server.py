#!/usr/bin/python3

# RPC Server (UDP)
# Author(s): Fama Seye, Awa Niang

import sys
import socket
import xdr      # module provided by teacher in VPL
import rpcnet   # module provided by teacher in VPL
import rpcmsg   # module provided by teacher in VPL
import rpcbind  # module provided by teacher in VPL

###############################################
###              CONSTANTS                  ###
###############################################

TEST_PROG = 0x20000001
TEST_VERS = 1

PROC_NULL = 0
PROC_PI = 1
PROC_INC = 2
PROC_ADD = 3
PROC_ECHO = 4

###############################################
###             PROCEDURE                   ###
###############################################
def null():
    return b''  

def pi():
    return xdr.encode_double(3.1415926)

def inc(x):
    return xdr.encode_int(x + 1)

def add(x, y):
    return xdr.encode_int(x + y)

def echo(s):
    return xdr.encode_string(s)

def handle(xid,prog,vers,proc,args):
    
    if proc == PROC_NULL: 
        response =null()
            
    elif proc == PROC_PI:  
        response = pi()
    
    elif proc == PROC_INC: 
            x = xdr.decode_int(args)
            response = inc(x)
    
    elif proc == PROC_ADD:  
            x, y = xdr.decode_two_int(args)
            response =add(x,y)
    
    elif proc == PROC_ECHO: 
            s = xdr.decode_string(args)
            response = echo(s)
    
    else:
        raise ValueError(f"Proc incorrect")
        
    return response
###############################################
###                 MAIN                    ###
###############################################

if (len(sys.argv) != 2) :
    print("Usage: server.py <port>")
    sys.exit(1)

host = ''
port = int(sys.argv[1])

#Creation d'une socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))

#Enregistrement du programme de numéro 0x20000001 (version 1)
xid=3333
rpcbind.register(xid, TEST_PROG, TEST_VERS, port) 

#Le serveur est continuellement à l'écoute, s'il reçoit une requête, il execute la procédure concernée  
while True:
   rpcnet.reply(sock,handle)
sock.close()
# EOF