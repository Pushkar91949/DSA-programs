def mostWater(height):
    left = 0
    right = len(height) - 1
    maxWater = 0
    while left < right:
        waterNow = min(height[left], height[right]) * (right - left)
        maxWater = max(maxWater, waterNow)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxWater


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(mostWater(heights))
