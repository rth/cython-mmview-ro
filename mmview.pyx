cpdef getmax(double[:] x):
    """Example code, should work with both
    ro and rw memoryviews"""
    cdef double max_val = -float('inf')
    for val in x:
        if val > max_val:
            max_val = val
    return max_val


cpdef update_array(double [:] x):
    """Modifying a ro memoryview should raise an error"""
    x[0] = 23.


cpdef getconst(const double [:] x):
    """Should only accept ro memoryviews"""
    return x[0]


cpdef double [:] inner_func(double [:] x):
    print('Received x[0]=', x[0])
    x[0] = -99.
    print('Changed to x[0]=', x[0])
    print('Memorymap modified in inner function.',
          'Recieved x.base.flags.writeable:',
          x.base.flags.writeable)
    return x
    

cpdef outer_func(double [:] x):
    cdef double [:] y = inner_func(x)
    return y

