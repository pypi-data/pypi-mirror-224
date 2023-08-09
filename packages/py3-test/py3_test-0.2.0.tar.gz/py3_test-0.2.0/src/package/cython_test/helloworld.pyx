def print_test1(aaa):
    return aaa


cdef print_test2(str aaa):
    return aaa

cdef extern from "c_helloworld.c":
    int c_fib(int n)

def print_test3(n):
    return c_fib(n)


def print_dict(dict aaa):
    return aaa
