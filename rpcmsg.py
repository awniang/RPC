#!/usr/bin/python3

# RPC Message Module
# Author(s):

import xdrlib

###############################################
###             RPC CONSTANTS               ###
###############################################

CALL = 0
REPLY = 1
RPC_VERSION = 2
AUTH_NONE = 0
MSG_ACCEPTED = 0
MSG_DENIED = 1
SUCCESS = 0

###############################################
###             ENCODE CALL                 ###
###############################################

def encode_call(xid, prog, vers, proc, data) -> bytes:
    """
    >>> encode_call(1, 1, 1, 1, b'ABCD').hex()
    '0000000100000000000000020000000100000001000000010000000000000000000000000000000041424344'
    """
    msg = b''
    msgtype =cred = verf =0
    rpcvers =  2
    p = xdrlib.Packer()
    p.pack_uint(xid)
    p.pack_uint(msgtype)
    p.pack_uint(rpcvers)
    p.pack_uint(prog)
    p.pack_uint(vers)
    p.pack_uint(proc)
    p.pack_uint(cred)
    p.pack_uint(cred)
    p.pack_uint(verf)
    p.pack_uint(verf)
    p.pack_fopaque(len(data),data)
    msg = p.get_buffer()
    return msg

###############################################
###             ENCODE REPLY                ###
###############################################

def encode_reply(xid, data) -> bytes:
    """
    >>> encode_reply(1, b'ABCD').hex()
    '00000001000000010000000000000000000000000000000041424344'
    """
    msg = b''
    msgtype = 1
    reply_state = verf = accept_state = 0
    p = xdrlib.Packer()
    p.pack_uint(xid)
    p.pack_uint(msgtype)
    p.pack_uint(reply_state)
    p.pack_uint(verf)
    p.pack_uint(verf)
    p.pack_uint(accept_state)
    p.pack_fopaque(len(data),data)
    msg = p.get_buffer()
    return msg

###############################################
###            DECODE CALL                  ###
###############################################

def decode_call(msg : bytes):
    """
    >>> msg = bytes.fromhex('0000000100000000000000020000000100000001000000010000000000000000000000000000000041424344') ; decode_call(msg)
    (1, 1, 1, 1, b'ABCD')
    """
    xid  = prog = vers = proc  = 0
    data = b''
    unpack = xdrlib.Unpacker(msg)
    xid = unpack.unpack_uint()
    unpack.unpack_uint() #msgtype
    unpack.unpack_uint() #rpcvers
    prog = unpack.unpack_uint()
    vers = unpack.unpack_uint()
    proc = unpack.unpack_uint()
    unpack.unpack_uint() #cred
    unpack.unpack_uint() #cred
    unpack.unpack_uint() #verf
    unpack.unpack_uint() #verf
    data = unpack.unpack_fopaque(len(msg)-40)
    return (xid, prog, vers, proc, data)

###############################################
###             DECODE REPLY                ###
###############################################

def decode_reply(msg):
    """
    >>> msg = bytes.fromhex('00000001000000010000000000000000000000000000000041424344') ; decode_reply(msg)
    (1, b'ABCD')
    """
    xid = 0
    data = b''
    unpack = xdrlib.Unpacker(msg)
    xid = unpack.unpack_uint()
    unpack.unpack_uint() #reply_state
    unpack.unpack_uint() #msgtype
    unpack.unpack_uint() #verf
    unpack.unpack_uint() #verf
    unpack.unpack_uint() #accept_state
    data = unpack.unpack_fopaque(len(msg)-24)
    return (xid, data)

###############################################
###                MAIN                     ###
###############################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF