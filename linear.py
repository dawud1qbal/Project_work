#Linear search in python
def linearSearch(array, n, x):
    #going through array sequentially
    for i in range(0, n): # for loop
        if (array[i] == x):
            return i
    return -1

array = [2, 4, 0, 1, 9] # this is the list of the array
x = 1 # 1 is stored in variable inside x
n = len(array)
result = linearSearch(array, n, x)
if(result == -1): #results written in an if statement
    print("Element not found") # this is a print statement saying if it is true it will output the elemnt found
else: # else loop
    print("Element found at index: ", result) # if not it will say this