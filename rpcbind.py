#!/usr/bin/python3

# RPC Bind Module
# Author(s): Fama Seye, Awa Niang

import xdrlib
import xdr      # module provided by teacher in VPL
import rpcnet   # module provided by teacher in VPL
import rpcmsg   # module provided by teacher in VPL

###############################################
###           CONSTANTS                     ###
###############################################

RPCB_HOST = "localhost"
RPCB_PORT = 111
RPCB_PROG = 100000 # rpcbind / portmap
RPCB_VERS = 4

RPCBPROC_SET = 1
RPCBPROC_UNSET = 2
RPCBPROC_GETADDR = 3

###############################################
###                GETPORT                  ###
###############################################

def getport(xid, prog, vers):
    #En cas d'erreur le port par défaut est -1
    port =-1
    
    #on appelle la procedure getaddr qui donne le resultat sous la forme 127.0.0.1.x.y
    data = xdr.encode_uint(prog) + xdr.encode_uint(vers) + xdr.encode_string("udp")
    response = rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_GETADDR, data)
    uaddr = xdr.decode_string(response)
    
    try:
    #on recupere x et y et on fait le calcul pour retrouver le port    
        parts = uaddr.split('.')
        port = int(parts[-2]) * 256 + int(parts[-1])
    except Exception as e:
        print(f"Error: {e}")
        return port
    return port

###############################################
###                 REGISTER                ###
###############################################

def register(xid, prog, vers, port) -> bool:
  try:
    #on remet l'adresse sous la forme 127.0.0.1.x.y   
    uaddr = f"{RPCB_HOST}.{port // 256}.{port % 256}"
    
    #on appelle la procédure SET
    data = xdr.encode_uint(prog) + xdr.encode_uint(vers) + xdr.encode_string("udp") + xdr.encode_string(uaddr) + xdr.encode_string("")
    response = rpcnet.call(RPCB_HOST, 111, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_SET, data)

    #on vérifie si l'enregistrement est réussi sinon on supprime le programme puis on le réenregistre
    success = xdr.decode_bool(response)
    if not success:
            unreg = unregister(xid, prog, vers)
            if unreg:
                res=rpcnet.call(RPCB_HOST, RPCB_PORT, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_SET, data)
                success2 = xdr.decode_bool(res)
                return success2
    return success
  except Exception as e:
      print(e)
      return False
###############################################
###              UNREGISTER                 ###
###############################################

def unregister(xid, prog, vers) -> bool:
        
    #on appelle la procédure UNSET    
    data = xdr.encode_uint(prog) + xdr.encode_uint(vers) + xdr.encode_string("udp") + xdr.encode_string("") + xdr.encode_string("")
    response = rpcnet.call(RPCB_HOST, 111, xid, RPCB_PROG, RPCB_VERS, RPCBPROC_UNSET, data)
    
    #on vérifie si la suppression est réussie
    success = xdr.decode_bool(response)
    return success

# EOF
