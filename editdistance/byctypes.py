# -*- coding: utf-8 -*-
import os

import ctypes
dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_editdistance.so'))


def eval(a, b):
    al = [hash(x) for x in a]
    bl = [hash(x) for x in b]
    aarr = ctypes.c_int64 * len(al)
    barr = ctypes.c_int64 * len(bl)
    ap, bp = aarr(*al), barr(*bl)
    return dll.edit_distance(ctypes.byref(ap), len(al), ctypes.byref(bp), len(bl), 0)
