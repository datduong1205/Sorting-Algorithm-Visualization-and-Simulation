# Name: Le Minh Dat Duong
# ID: 100886108
# Assignment 2 - Data Structure and Algorithms

import time
import sys

def MergeSort(arr):
    if len(arr) > 1:
        print('Dividing:', arr)
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        MergeSort(left_arr)
        MergeSort(right_arr)

        i = 0
        j = 0
        count = 0   
        print(f'Merging:', left_arr, right_arr)
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[count] = left_arr[i]
                i += 1
            else:
                arr[count] = right_arr[j]
                j += 1
            count += 1
                
        # Checking if any element was left
        while i < len(left_arr):
            arr[count] = left_arr[i] 
            i += 1
            count += 1
        
        while j < len(right_arr):
            arr[count] = right_arr[j]
            j += 1
            count += 1
    else:
        return arr
    
    return arr

def QuickSort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    print(arr, ',', pivot, 'is pivot')
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    new_arr = QuickSort(items_lower) + [pivot] + QuickSort(items_greater)
    print(new_arr)

    return new_arr 

def analyzeSortPerformance(data, description, time_complexity):
    print(f"{description} - Starting array: {data}")
    start = time.time()
    QuickSort(data.copy())
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    print(f"Time Complexity: {time_complexity}\n")


if __name__ == '__main__':
    product_id = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    product_id_sorted = [1, 2, 4, 6, 7, 11, 15, 23, 29, 30, 51, 67, 89, 118]
    product_id_reversed = [118, 89, 67, 51, 30, 29, 23, 15, 11, 7, 6, 4, 2, 1]

    while True:

        choice = int(input('Please choose sorting algorithm:\n1. Merge Sort\n2. Quick Sort\n3. Exit\nChoose: '))
        if choice == 1:
            analyzeSortPerformance(product_id_sorted, MergeSort,'Best Case (Sorted)', 'Ω(n log(n))')
            analyzeSortPerformance(product_id, MergeSort,'Average Case (Manually Shuffle)', 'Θ(n log(n))')
            analyzeSortPerformance(product_id_reversed, MergeSort,'Worst Case (Reverse Sorted)', 'O(n log(n))')
            print('--------------------------------------------------------------------------------------------------')

        elif choice == 2:
            analyzeSortPerformance(product_id_sorted,'Best Case (Sorted)', 'Ω(n log(n))')
            analyzeSortPerformance(product_id,'Average Case (Manually Shuffle)', 'Θ(n log(n))')
            analyzeSortPerformance(product_id_reversed,'Worst Case (Reverse Sorted)', 'O(n^2)')
            print('--------------------------------------------------------------------------------------------------')

        elif choice == 3:
            print('Exit!')
            break

        else: 
            print('Option does not exist! Please choose again.')
