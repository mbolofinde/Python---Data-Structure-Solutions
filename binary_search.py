# Solution for Binary Search Algorith with Python


def binary_search(arr, target):
    low, high = 0, len(arr) - 1   # define the start and end location of the array
    while low <= high:
        mid = (low+high) // 2 
        mid_value = arr[mid]        # Begin with the mid index for the comparison. 
        if mid_value == target:
            return mid
        elif mid_value > target: 
            high = mid - 1
        else:
            low = mid + 1
    return -1


my_list = [1, 2, 3, 4, 5]
target_value = 3
result = binary_search(my_list, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}')
else: 
    print(f' Target {target_value} not found in the array')

