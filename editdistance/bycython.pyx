# distutils: language = c++
# distutils: sources = editdistance/_editdistance.cpp

from libc.stdlib cimport malloc, free

cdef extern from "_editdistance.h":
    unsigned int edit_distance(const long *a, const unsigned int asize, const long *b, const unsigned int bsize)

cpdef unsigned int eval(object a, object b):
    cdef unsigned int i, dist
    cdef long *al = <long *>malloc(len(a) * sizeof(long))
    for i in range(len(a)):
        al[i] = hash(a[i])
    cdef long *bl = <long *>malloc(len(b) * sizeof(long))
    for i in range(len(b)):
        bl[i] = hash(b[i])
    dist = edit_distance(al, len(a), bl, len(b))
    free(al)
    free(bl)
    return dist
