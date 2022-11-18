# In this script, we will test the speed of our different sorting methods.
# The maxpysort package offers 4 sorting methods:
# - sort_base, written using base Python functions
# - sort_numpy, using the numpy sorting function
# - sort_c, using C code
# - sort_cpp, using C++ code
# In this script, we will create two unsorted lists of random numbers,
# one of relatively small size and one of much greater size,
# and use each method to sort the arrays while timing how long each takes with the task.

import copy
import timeit
import random
from maxpysort.sort_python import sort_base, sort_numpy
from maxpysort.sort_c import sort_c
from maxpysort.sort_cpp import sort_cpp

# Case 1: small list
small_list = [random.random() for i in range(100)]

small_base_time = timeit.timeit("sort_base(l)",
                                setup="l = copy.deepcopy(small_list)",
                                globals=globals(),
                                number=5)
small_numpy_time = timeit.timeit("sort_numpy(l)",
                                 setup="l = copy.deepcopy(small_list)",
                                 globals=globals(),
                                 number=5)
small_c_time = timeit.timeit("sort_c(l)",
                             setup="l = copy.deepcopy(small_list)",
                             globals=globals(),
                             number=5)
small_cpp_time = timeit.timeit("sort_cpp(l)",
                               setup="l = copy.deepcopy(small_list)",
                               globals=globals(),
                               number=5)
print("Scenario 1: Sort list of 100 items")
print(f"Base Python: {small_base_time}")
print(f"Numpy: {small_numpy_time}")
print(f"C: {small_c_time}")
print(f"C++: {small_cpp_time}")

# Case 2: big list
big_list = [random.random() for i in range(int(1e6))]

small_base_time = timeit.timeit("sort_base(l)",
                                setup="l = copy.deepcopy(big_list)",
                                globals=globals(),
                                number=5)
small_numpy_time = timeit.timeit("sort_numpy(l)",
                                 setup="l = copy.deepcopy(big_list)",
                                 globals=globals(),
                                 number=5)
small_c_time = timeit.timeit("sort_c(l)",
                             setup="l = copy.deepcopy(big_list)",
                             globals=globals(),
                             number=5)
small_cpp_time = timeit.timeit("sort_cpp(l)",
                               setup="l = copy.deepcopy(big_list)",
                               globals=globals(),
                               number=5)
print("Scenario 2: Sort list of 1M items")
print(f"Base Python: {small_base_time}")
print(f"Numpy: {small_numpy_time}")
print(f"C: {small_c_time}")
print(f"C++: {small_cpp_time}")
