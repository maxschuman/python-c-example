from maxpysort.sort_python import sort_base, sort_numpy
from maxpysort.sort_c import sort_c
from maxpysort.sort_cpp import sort_cpp

array_1 = [1, 2, 3, 4]
array_2 = [1.1, 2.2, 3.3, 4.4]
array_3 = [4, 2, 1, 3]
array_4 = [2.2, 1.1, 1.6]
array_5 = [5.3]
array_6 = []


def test_sort_base():
    assert sort_base(array_1) == [1, 2, 3, 4]
    assert sort_base(array_2) == [1.1, 2.2, 3.3, 4.4]
    assert sort_base(array_3) == [1, 2, 3, 4]
    assert sort_base(array_4) == [1.1, 1.6, 2.2]
    assert sort_base(array_5) == [5.3]
    assert sort_base(array_6) == []

def test_sort_numpy():
    assert sort_numpy(array_1) == [1, 2, 3, 4]
    assert sort_numpy(array_2) == [1.1, 2.2, 3.3, 4.4]
    assert sort_numpy(array_3) == [1, 2, 3, 4]
    assert sort_numpy(array_4) == [1.1, 1.6, 2.2]
    assert sort_numpy(array_5) == [5.3]
    assert sort_numpy(array_6) == []

def test_sort_c():
    assert sort_c(array_1) == [1, 2, 3, 4]
    assert sort_c(array_2) == [1.1, 2.2, 3.3, 4.4]
    assert sort_c(array_3) == [1, 2, 3, 4]
    assert sort_c(array_4) == [1.1, 1.6, 2.2]
    assert sort_c(array_5) == [5.3]
    assert sort_c(array_6) == []

def test_sort_cpp():
    assert sort_cpp(array_1) == [1, 2, 3, 4]
    assert sort_cpp(array_2) == [1.1, 2.2, 3.3, 4.4]
    assert sort_cpp(array_3) == [1, 2, 3, 4]
    assert sort_cpp(array_4) == [1.1, 1.6, 2.2]
    assert sort_cpp(array_5) == [5.3]
    assert sort_cpp(array_6) == []