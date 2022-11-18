from ctypes import c_double, c_int, CDLL
import os

# Load sorting function from C folder
cpp_path = f'{os.path.dirname(__file__)}/C++/quicksort.so'
quicksort_lib = CDLL(cpp_path)
cpp_quicksort = quicksort_lib.cpp_quicksort
cpp_quicksort.restype = None

def sort_cpp(array_in):
    length = len(array_in)
    cpp_array = (c_double * length)(*array_in)
    print(cpp_array[:])
    cpp_quicksort(cpp_array, c_int(length))
    return cpp_array[:]