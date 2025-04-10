def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i+1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

# Example usage:
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted list using Selection Sort:", my_list)
