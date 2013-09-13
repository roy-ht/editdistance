# distutils: language = c++
# distutils: sources = editdistance/_editdistance.cpp

from libc.stdlib cimport malloc, free

cdef extern from "editdistance/_editdistance.h":
    unsigned int edit_distance(const long long *a, const unsigned int asize, const long long *b, const unsigned int bsize)

cpdef unsigned int eval(object a, object b):
    cdef unsigned int i, dist
    cdef long long *al = <long long *>malloc(len(a) * sizeof(long long))
    for i in range(len(a)):
        al[i] = hash(a[i])
    cdef long long *bl = <long long *>malloc(len(b) * sizeof(long long))
    for i in range(len(b)):
        bl[i] = hash(b[i])
    dist = edit_distance(al, len(a), bl, len(b))
    free(al)
    free(bl)
    return dist
