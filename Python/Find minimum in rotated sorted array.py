def minimum(arr):
    l, r = 0, len(arr) - 1
    result = arr[0]

    while l <= r:
        if arr[l] < arr[r]:
            result = min(result, arr[l])
            break
        mid = (l + r) // 2
        result = min(arr[mid], result)
        if arr[mid] >= arr[l]:
            l = mid + 1
        else:
            r = mid - 1
    return result
array = [7,8,9,1,2,3,4,5,6]
print(minimum(array))
