import xdr
import rpcnet

HOST = "localhost"
PORT = 7777
TEST_PROG = 0x20000001
TEST_VERS = 1
PROC_ADD = 3
XID = 1000

args = xdr.encode_two_int(10, 20)
result = rpcnet.call(HOST, PORT, XID, TEST_PROG, TEST_VERS, PROC_ADD, args)
print("result =", xdr.decode_int(result))