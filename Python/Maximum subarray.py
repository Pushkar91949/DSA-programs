# BRUTE FORCE APPROACH
# NOT EFFICIENT FOR LARGER ARRAYS
# TIME COMPLEXITY = O(N^3)
# SPACE COMPLEXITY = O(1)

import math


def max_sub_arr_BRUTE_FORCE(arr):
    n = len(arr)
    ans = -math.inf
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            ans = max(ans, curr_sum)
    return ans


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Max subarray sum = ", max_sub_arr_BRUTE_FORCE(arr))

# # We need to use Kadane's algorithm for this problem.

# KADANE'S ALGORITHM

# print(max_sub_arr([1,-2,3,1,-3,-3,43,43,4,354,-345,32]))


def kadanes_algorithm(arr):
    curr_max = global_max = arr[0]
    n = len(arr)
    for i in range(1, n):
        curr_max = max(arr[i], curr_max+arr[i])
        global_max = max(global_max, curr_max)
    return global_max


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanes_algorithm(arr)
print("Maximum subarray sum: ", result)

# ALTERNATIVE APPROACH FOR KADANE"S ALGORITHM:

def maxSubArray(self, nums: List[int]) -> int:
    ans = -inf
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if ans < curr_sum:
            ans = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return ans
