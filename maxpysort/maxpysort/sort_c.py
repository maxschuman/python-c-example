from ctypes import c_double, c_int, CDLL
import os

# Load sorting function from C folder
c_path = f'{os.path.dirname(__file__)}/C/quicksort.so'
quicksort_lib = CDLL(c_path)
c_quicksort = quicksort_lib.c_quicksort
c_quicksort.restype = None

def sort_c(array_in):
    length = len(array_in)
    c_array = (c_double * length)(*array_in)
    print(c_array[:])
    c_quicksort(c_array, c_int(length))
    return c_array[:]