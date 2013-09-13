# -*- coding: utf-8 -*-
import os

import ctypes
dll = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_editdistance.so'))
dll.edit_distance.resttype = ctypes.c_uint
dll.edit_distance_by_patternmap.resttype = ctypes.c_uint


def eval(a, b):
    al = [hash(x) for x in a]
    bl = [hash(x) for x in b]
    aarr = ctypes.c_int64 * len(al)
    barr = ctypes.c_int64 * len(bl)
    ap, bp = aarr(*al), barr(*bl)
    return dll.edit_distance(ctypes.byref(ap), len(al), ctypes.byref(bp), len(bl))


class PatternMap(ctypes.Structure):
    _arr_bit_vector = ctypes.c_uint64 * 4
    _fields_ = [('p_', _arr_bit_vector * 256), ('tmax_', ctypes.c_uint), ('tlen_', ctypes.c_uint)]


class EditDistance():
    '''sequence size is limited to 255'''
    def __init__(self, s):
        if len(s) > 255:
            raise ValueError('size of your sequence length must be < 256')
        self._m = {}
        for e in s:
            self._m.setdefault(e, len(self._m))
        sl = [self._m[x] for x in s]
        sarr = ctypes.c_int64 * len(sl)
        sp = sarr(*sl)
        self._pm = PatternMap()
        dll.create_patternmap(ctypes.byref(self._pm), ctypes.byref(sp), len(sl))

    def measure(self, s):
        sl = [self._m.get(x, 255) for x in s]
        sarr = ctypes.c_int64 * len(sl)
        sp = sarr(*sl)
        r = dll.edit_distance_by_patternmap(ctypes.byref(self._pm), ctypes.byref(sp), len(sl))
        return r
