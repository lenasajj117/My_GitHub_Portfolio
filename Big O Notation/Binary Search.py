#implementation
def binary_search(lst, target):
    start = 0
    end = len(lst) -1
    while(start <= end):
        mid = (start + end) // 2
        if(lst[mid] > target):
            end = mid - 1
        elif(lst[mid] < target):
            start = mid + 1
        else:
            return mid
    return None
numbers = [11, 23, 36, 47, 51, 66, 73, 83, 92]
target1 = 23
target2 = 83
print("The index returned for", target1, "is",binary_search(numbers,target1))
print("The index returned for", target2, "is",binary_search(numbers,target2))
