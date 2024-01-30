def rever(arr):
    n = len(arr)
    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n - 1 - i]
        arr[n - i - 1] = temp
    return arr

# The above approach to reverse an array iterates until half the length of an array and swaps the first element with the last element,
# second element with the second last element until it reaches the middle of the array, like this the array is revered.
# When the last element is set as first element, the first element is temporarily stored in a temp variable. Which is later set to the
# last element.


def rev(arr):
    n = len(arr)
    temp = []
    for i in range(n-1, -1, -1):
        temp.append(arr[i])
    return temp

# The above approach to revrse an array is less efficient in terms of space as is uses an entire new array.
# We iterate through the old array from the last element to the first element and we keep adding the element in the temp array.


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arraynew = [11, 12, 13, 14, 15, 16, 17, 18, 19]
print(rever(array))
print(rev(arraynew))
