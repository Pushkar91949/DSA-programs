import math
def maxProduct(nums):
    maxi = -math.inf
    prefix,suffix = 1,1

    n = len(nums)
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n - i - 1]

        maxi = max(maxi, max(prefix, suffix))
    return maxi

nums = [2,3,-2,4]
print(maxProduct(nums))
