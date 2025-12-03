#insertion sort in python

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        #for descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        #place key at after the element just smaller than it
        array[j + 1] = key

data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted array in ascedning order:')
print(data)