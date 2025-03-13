import numpy as np


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    arr = np.array(arr)
    p = arr[len(arr) // 2]
    left = [x for x in arr if x < p]
    middle = [x for x in arr if x == p]
    right = [x for x in arr if x > p]
    return quicksort(left) + middle + quicksort(right)

# h = [42 , 3 , 1 , 5 , 53 , 7 , 2 , 87 , 0]
# print(list(quicksort(h)))
