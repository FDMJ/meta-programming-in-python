# O(n)
# this algos runtime will grow linear to the amount of data
def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False