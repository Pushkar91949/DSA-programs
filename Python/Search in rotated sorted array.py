# Search in rotated sorted array
# TIME COMPLEXITY : O(log(n))

# The brute force linear search approach takes O(n) time but binary search approach is O(log(n)) which is more efficient.

def search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid

        elif arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


array = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
target = 10
res = search(array, target)
print("Element", target, "found at index ", res)
