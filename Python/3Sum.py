def threeSum(nums):
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            threeSum = a + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return res


array = [-1, 0, 1, 2, -1, -4]
print(threeSum(array))


# Time complexity = O(n^2).
# O(nlogn) for sorting and O(n^2) when we run two loops, one inside another.) --> O(nlogn) + O(n^2) = O(n^2).

# We take each element of nums and firs element of the triplet one by one. When the 1st element is set, we just need 2 more elements which we get by using 2 pointers, 
# left and right (as we have already sorted the array). if sum of first element, nums[left] and nums[right] == 0: We add [a, nums[left], nums[right]] to our result array.
# This process is done for each and every element when it is set as first element, it is not necessary that we find a solution for all the elements when they are set as first.
