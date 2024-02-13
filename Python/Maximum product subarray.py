import math
def maxProduct(nums):
    maxi = -math.inf
    prod = 1

    for i in range(len(nums)):
        prod *= nums[i]
        maxi = max(prod,maxi)
        if prod == 0:
            prod = 1
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        prod *= nums[i]

        maxi = max(prod,maxi)
        if prod == 0:
            prod = 1
    return maxi

nums = [2,3,-2,4]
print(maxProduct(nums))