# maxpysort

This is a package that demonstrates incorporating C code into Python code for increased speed.

To install the package, use pip:

`pip install .`

Additionally, make sure that the C dependency referenced in the package has been compiled:

```
cd maxpysort/C
gcc -o quicksort.so -shared -fPIC -O2 quicksort.c
```

And make sure that the C++ dependency in the package has been compiled as well:

```
cd ../C++
g++ -fPIC -shared -o quicksort.so quicksort.cpp
```

To test the code, go to the root of the package and run the `pytest` command at the command line.

To evaluate the speed of the different sorting algorithms, you can run the `scripts/speed_test.py` script. 