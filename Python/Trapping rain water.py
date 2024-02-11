def TrappingRainWater(heights):
    if not heights:
        return 0

    l, r = 0, len(heights)-1
    left_max, right_max = heights[l], heights[r]

    ans = 0

    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, heights[l])
            ans += left_max - heights[l]
        else:
            r -= 1
            right_max = max(right_max, heights[r])
            ans += right_max - heights[r]
    return ans


print(TrappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
