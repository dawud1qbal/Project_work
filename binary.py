# Binary search in python

def binarySearch(array, x, low, high):
    #repeat until the pointerslow and high meet each other
    while low <= high:
        mid = low + (high - low)//2

        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4
reuslt = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(resutlt))
else:
    print("Not found")