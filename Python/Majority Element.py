def majorityElement(nums):
    d = {}
    result = majority = 0

    for num in nums:
        d[num] = 1 + d.get(num, 0)
        if d[num] > majority:
            result = num
            majority = d[num]
    return result

print(majorityElement([2,3,4,5,6,6,6,7,6,6,6,6]))

