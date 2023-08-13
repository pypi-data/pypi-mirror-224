'''
A Python module with data analyst functions. Designed to be a toolbox for the Data Analyst to use.
'''
import numpy as np

def transpose2d(input_matrix: list[list[float]]) -> list:
    '''
    Function that will transpose any 2 dimensional matrix.

    Arguments:
        input_matrix - a list of lists of floats, that represents a 2D matrix.
    
    Returns:
        result - a list of lists of floats, that represents a result of transposiotion of a
        2D matrix.
    '''

    result = [[input_matrix[j][i]
               for j in range(len(input_matrix))]
               for i in range(len(input_matrix[0]))]
    return result

def window1d(input_array: list | np.ndarray,
             size: int,
             shift: int = 1,
             stride: int = 1
            ) -> list[list | np.ndarray]:
    '''
    Function that picks subsets of a 1D array and gives back the set of windows.

    Arguments:
        input_array - a list of elements or numpy.ndarray
        size - the size of windows
        shift (defaults to 1) - determines the number of input elements to shift between the start
                                of each window
        stride (defaults to 1) - determines the stride between input elements within a window
    
    Returns:
        windows - set of windows, that contains a subset of elements of the input dataset
    '''

    result = [[input_array[i]
               for i in range(j, size*stride+j, stride)]
               for j in range(0, len(input_array)-(size-1)*stride, shift)]
    return result

def convolution2d(input_matrix: np.ndarray,
                  kernel: np.ndarray,
                  stride : int = 1
                  ) -> np.ndarray:
    '''
    A function, that calculates a 2d convolution result from numpy.arrays

    Arguments:
        input_matrix - a first of two matrices that is required to calculate convolution matrix
        kernel - a second of two matrices that is required to calculate convolution matrix
        stride - how many elements should each step be separated with
    
    Returns:
        numpy.array, the convolution result calculated from input matrices (input_matrix and kernel)
    '''

    kernel_rows, kernel_cols = kernel.shape
    input_rows, input_cols = input_matrix.shape

    kernel = np.fliplr(np.flipud(kernel))

    row, col = 0, 0
    result = np.array([])
    while row + kernel_rows <= input_rows:
        col = 0
        result_row = np.array([])
        while col + kernel_cols <= input_cols:
            input_matrix_slice = input_matrix[row:row+kernel_rows, col:col+kernel_cols]
            convolution_result = np.multiply(input_matrix_slice, kernel).sum()
            result_row = np.append(result_row, convolution_result)
            col = col + stride
        result = np.vstack((result, result_row)) if result.size else result_row
        row = row + stride

    return result
