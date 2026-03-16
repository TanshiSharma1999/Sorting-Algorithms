# Selection Sort is a simple sorting algorithm. 
# It repeatedly selects the smallest (or largest) element from the unsorted part of the array and places it in the correct position.

#sorts min to max
def selectionSort(array, size):
    for ind in range(size - 1):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[ind], array[min_index] = array[min_index], array[ind]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)

print("Sorted Smallest to Largest: ",arr)

#sorts max to min
def selectionSort(array, size):
    for ind in range(size - 1):
        max_index = ind

        for j in range(ind + 1, size):
            if array[j] > array[max_index]:
                max_index = j

        array[ind], array[max_index] = array[max_index], array[ind]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)

print("Sorted  Largest to Smallest : ",arr)
