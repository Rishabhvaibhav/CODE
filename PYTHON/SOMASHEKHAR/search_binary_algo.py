def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
arr = [11,23,45,56,78,89]
target = 45
result = binary_search(arr, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the array")