import numpy as np

def count_sequence_occurrences(arr, seq):
    str_arr = np.array2string(arr)
    return str_arr.count(seq)

# Example usage:
arr = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
seq = "[1, 2, 3]"
result = count_sequence_occurrences(arr, seq)
print(result)
