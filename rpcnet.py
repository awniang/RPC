#!/usr/bin/python3

# RPC Net Module
# Author(s): Awa Niang, Fama Seye

import socket
import rpcmsg

###############################################
###           CONSTANTS                     ###
###############################################

MAXMSG = 1500

###############################################
###                CALL UDP                 ###
###############################################

def call(host, port, xid, prog, vers, proc, args) -> bytes:
    
    #Creation d'une socket UDP
    client_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_s.settimeout(2)
    
    result = b''
    
    #Encodage et envoi de la requete au serveur
    msg = rpcmsg.encode_call(xid,prog,vers,proc,args)
    client_s.sendto(msg,(host,port))
    
    try :
    #Reception et decodage de la reponse du serveur    
        response, _ = client_s.recvfrom(MAXMSG)
        _, data = rpcmsg.decode_reply(response)
        result = data
    except Exception as e:
        print(f"Error: {e}")
        client_s.close()
    return result


###############################################
###               REPLY UDP                 ###
###############################################

def reply(sserver, handle):
    try :
    #Reception et decodage de la requete du client     
        msg,addr = sserver.recvfrom(MAXMSG)
        xid, prog, vers, proc, args = rpcmsg.decode_call(msg)
    
    #Application de la procédure concernée et envoi du resultat au client    
        data = handle(xid,prog,vers,proc,args)
        response_message = rpcmsg.encode_reply(xid,data)
        sserver.sendto(response_message,addr)
    except Exception as e :
        print(f"Error in reply: {e}")
        



# EOF
