
import struct

# packing keys in 4/8 bytes for lmdb indices
# databases are created with integerkey=True, so keys must be all same size and native
# byte order unsigned (4 bytes, @I) or size_t (8 bytes, @Q)

KEYPACK4 = '@I'
KEYPACK8 = '@Q'

def nr_key4(nr):
    return struct.pack(KEYPACK4, nr)


def key4_nr(key):
    return struct.unpack(KEYPACK4, key)[0]


def key4_ge(k1, k2):
    # compare two keys which are native byte order, so little endian on M1
    # start with high byte
    x = len(k1)
    while x > 0:
        x -= 1
        if k1[x] < k2[x]:
            return False
    return True


def b2hex(ba):
    """binary to hex string"""
    return ''.join(['\\x{:02x}'.format(x) for x in ba])

