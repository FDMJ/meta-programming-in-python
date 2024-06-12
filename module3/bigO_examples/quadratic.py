# O(n^2)
# this algos time complexity will grow with the square of the input size
# as the input data increases, the runtime increases quadratically
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1 ] = arr[j + 1], arr[j]