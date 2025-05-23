#!/usr/bin/python3

# XDR Module
# Author(s): Fama Seye

import xdrlib

###############################################
###               XDR ENCODE                ###
###############################################

def encode_double(val) -> bytes:
    """
    >>> encode_double(1.2).hex()
    '3ff3333333333333'
    """
    data = b''
    
    pack = xdrlib.Packer()
    pack.pack_double(val)
    data = pack.get_buffer()
    
    return data

def encode_int(val) -> bytes:
    """
    >>> encode_int(-1).hex()
    'ffffffff'
    """
    data = b''
    
    pack = xdrlib.Packer()
    pack.pack_int(val)
    data = pack.get_buffer()
    
    return data

def encode_uint(val) -> bytes:
    """
    >>> encode_uint(10).hex()
    '0000000a'
    """
    data = b''
    
    pack = xdrlib.Packer()
    pack.pack_uint(val)
    data = pack.get_buffer()
    
    return data

def encode_bool(val : bool) -> bytes:
    """
    >>> encode_bool(True).hex()
    '00000001'
    """
    data = b''
    
    pack = xdrlib.Packer()
    pack.pack_bool(val)
    data = pack.get_buffer()
    return data

def encode_string(val: str) -> bytes:
    """
    >>> encode_string("hello").hex()
    '0000000568656c6c6f000000'
    """
    data = b''

    pack = xdrlib.Packer()
    pack.pack_string(val.encode('utf-8'))
    data = pack.get_buffer()

    return data

def encode_two_int(val1, val2) -> bytes:
    """
    >>> encode_two_int(-1,2).hex()
    'ffffffff00000002'
    """
    data = b''

    pack = xdrlib.Packer()
    pack.pack_int(val1)
    pack.pack_int(val2)
    data = pack.get_buffer()
   
    return data

###############################################
###             XDR DECODE                  ###
###############################################

def decode_double(data : bytes):
    """
    >>> msg = bytes.fromhex('3ff3333333333333') ; decode_double(msg)
    1.2
    """
    
    unpack=xdrlib.Unpacker(data)
    decoded=unpack.unpack_double()
    
    return decoded

def decode_int(data : bytes):
    """
    >>> msg = bytes.fromhex('ffffffff') ; decode_int(msg)
    -1
    """
    unpack=xdrlib.Unpacker(data)
    decoded=unpack.unpack_int()
    
    return decoded

def decode_uint(data : bytes):
    """
    >>> msg = bytes.fromhex('00000001') ; decode_uint(msg)
    1
    """
    
    unpack=xdrlib.Unpacker(data)
    decoded=unpack.unpack_uint()
    
    return decoded

def decode_bool(data : bytes):
    """
    >>> msg = bytes.fromhex('00000001') ; decode_bool(msg)
    True
    """
    
    unpack=xdrlib.Unpacker(data)
    decoded=unpack.unpack_bool()
    
    return decoded

def decode_string(data : bytes) -> str:
    """
    >>> msg = bytes.fromhex('0000000568656c6c6f000000') ; decode_string(msg)
    'hello'
    """
    unpack=xdrlib.Unpacker(data)
    decoded=unpack.unpack_string()
    
    return decoded.decode()

def decode_two_int(data):
    """
    >>> msg = bytes.fromhex('ffffffff00000002') ; decode_two_int(msg)
    (-1, 2)
    """
    unpack=xdrlib.Unpacker(data)
    val1=unpack.unpack_int()
    val2=unpack.unpack_int()
    
    return (val1,val2)

###############################################
###                MAIN                     ###
###############################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
