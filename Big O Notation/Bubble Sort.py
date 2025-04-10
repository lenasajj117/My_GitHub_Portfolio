#bubble sort
my_list = [64,34,25,12,22,11,90]

n = len(my_list)
swapped = True # initialize swapped as true to enter the loop

while swapped:
 swapped = False # Reset swapped for this pass
 for i in range(1,n):
   if my_list[i-1] > my_list[i]:
      # swap the elements
      my_list[i-1],my_list[i] = my_list[i], my_list[i-1]
      swapped = True # set swapped to true if a swap occurs

# Print the sorted list
print("sorted list is:",my_list)