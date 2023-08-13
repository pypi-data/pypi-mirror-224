# jakluz-DE2.1

jakluz-DE2.1 is a small set of functions useful for data analysis. It consist of transpose2d (transposing matrix), windows1d (windowing function for vectors) and convolution2d (convolution for matrices).

## Usage

```python
import jakluz-DE2.1

# transpose2d returns [[1, 2], [3, 4], [5, 6]], a transposition of "data" matrix
data = [[1, 3, 5], [2, 4, 6]]
transpose2d(data)

# returns [[0, 2], [2, 4]], a set of windows
data = range(5)
window1d(data, size=2, shift=2, stride=2)

# returns [[1, 3], [7, 9]], a convolution of "input_matrix" and "kernel"
input_matrix = array(range(1, 10)).reshape(3, 3)
kernel = ones((1, 1))
convolution2d(input_matrix, kernel, stride=2)
```

## Tests
Test file is included in the repository. It tests every function with different parameters. You can run the tests with:

```python
python3 tests.py
```