def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = []
        greater = []
        for element in arr[1:]:
            if element <= pivot:
                lesser.append(element)
            else:
                greater.append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Example usage:
my_list = [74, 45, 32, 22, 11]
sorted_list = quick_sort(my_list)
print("Sorted list using Quick Sort:", sorted_list)
