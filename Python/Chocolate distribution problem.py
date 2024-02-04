import math


def chocolateDistribution(arr, n, m):
    if n == 0 or m == 0 or n < m:
        return 0

    ans = math.inf
    arr.sort()
    for i in range(0, n - m + 1):
        mini, maxi = arr[i], arr[i + m - 1]
        gap = maxi - mini
        if gap < ans:
            ans = gap
    return ans


array = [12, 4, 7, 9, 2, 23, 25, 41,
         30, 40, 28, 42, 30, 44, 48,
         43, 50]
n = len(array)
m = 7
print("Min difference = ", chocolateDistribution(array, n, m))


# // Time complexity = O(n*log(n))
