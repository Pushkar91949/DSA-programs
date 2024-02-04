# BRUTE FORCE:
def contains_duplicate_brute_force(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return True
    return False


print(contains_duplicate_brute_force([1, 2, 3, 4]))

# The above approach check each element with every other element which is very inefficient.

# Time complexity = O(n^2)

##########################################

# USING SORTING


def contains_duplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Time complexity = O(nlog(n))
print(contains_duplicate([1, 2, 3, 1, 2, 4, 5, 6]))

##########################################

# USING SET:


def containsDuplicate(nums):
    present_elements = set()
    for val in nums:
        if val in present_elements:
            return True
        present_elements.add(val)
    return False


print(containsDuplicate([1, 2, 3, 1, 2, 4, 5, 6]))

# Time complexity of this set wala approach is O(n).
