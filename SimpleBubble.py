#It is a simple Bubble Sort Program
# It will keep comparing adjacent elements in the list and swap them if they are ordered correctly.
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


numbers = [50, 13, 8, 24, 2]
sorted_numbers = bubble_sort(numbers)

print(sorted_numbers)