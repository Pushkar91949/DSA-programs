def minmax(arr):
    n = len(arr)
    if n == 1:
        minimum, maximum = arr[0], arr[0]

    if arr[0] > arr[1]:
        minimum = arr[1]
        maximum = arr[0]
    else:
        minimum = arr[0]
        maximum = arr[1]
    for i in range(2, n):
        if arr[i] > maximum:
            maximum = arr[i]
        elif arr[i] < minimum:
            minimum = arr[i]
    return minimum, maximum

# This method find minimum and maximum of an array.
# First, we set the larger of the first two elements as max and smaller of the first two elements as min.
# Then, we iterate through the array from the 3rd element till the last element.
# If the element is larger than max, we update the max to that element and if the element is smaller than min, we update min
# to that element.
# At the end, we have found the smallest element(min) and the largest element(max) from the array in
# O(n) time complexity.
# The normal approach of sorting the array first and then giving the first element as smallest and last element as largest is
# a little bit slower and its time complexity is O(n*log(n))


array = [3, 4, 3, 456, 3, 54, 63, 5464, 45, 673, 5446, 467, 4567, 1]
print(minmax(array))
