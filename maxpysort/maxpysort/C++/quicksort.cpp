int quicksort_partition(double *array_in, int low_index, int high_index)
{
    double pivot_element = array_in[high_index];
    int pivot_index = low_index - 1;

    for(int j = low_index; j < high_index; j++)
    {
        if(array_in[j] < pivot_element)
        {
            pivot_index++;
            double temp = array_in[pivot_index];
            array_in[pivot_index] = array_in[j];
            array_in[j] = temp;
        }
    }

    pivot_index++;
    double temp = array_in[pivot_index];
    array_in[pivot_index] = array_in[high_index];
    array_in[high_index] = temp;

    return pivot_index;
}

void quicksort_recursive(double *array_in, int low_index, int high_index)
{
    if(low_index < high_index){
        int pivot_index = quicksort_partition(array_in, low_index, high_index);
        quicksort_recursive(array_in, low_index, pivot_index - 1);
        quicksort_recursive(array_in, pivot_index + 1, high_index);
    }
}

// extern "C" is used to signal to the C++ compiler that it should use the exact function name here
// Because C++ supports overloading function names with different inputs, the compiler modifies
// the name at compile time so overloaded functions can be given different names
// This ensures that the expected name is available to be referenced by our python code
extern "C" {
    void cpp_quicksort(double *array_in, int length)
    {
        // run quicksort algorithm to sort array_in in place
        quicksort_recursive(array_in, 0, length - 1);
    }
}