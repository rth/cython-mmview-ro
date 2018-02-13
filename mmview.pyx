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

