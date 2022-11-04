import numpy as np
import copy

def sort_base(array_in):
    array_sorted = copy.deepcopy(array_in)
    array_sorted = _quicksort(array_sorted, 0, len(array_sorted) - 1)
    return array_sorted

def sort_numpy(array_in):
    return list(np.sort(array_in))

def _quicksort(array_in, low_index, high_index):
    if (low_index < high_index):
        partition_index = _quicksort_partition(array_in, low_index, high_index)
        _quicksort(array_in, low_index, partition_index - 1)
        _quicksort(array_in, partition_index + 1, high_index)

    return array_in

def _quicksort_partition(array_in, low_index, high_index):
    pivot_element = array_in[high_index]
    pivot_index = low_index - 1

    for j in range(low_index, high_index):
        if array_in[j] < pivot_element:
            pivot_index += 1
            array_in[pivot_index], array_in[j] = array_in[j], array_in[pivot_index]

    pivot_index += 1
    array_in[pivot_index], array_in[high_index] = array_in[high_index], array_in[pivot_index]

    return pivot_index
