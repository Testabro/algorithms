from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list

  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # Create the lesser_than_pointer
  lesser_than_pointer = start
  
  # Start a for loop, use 'idx' as the variable
  for idx in range(start, end):
    # Check if the value at idx is less than the pivot
    if list[idx] < pivot_element:
    # If so: 
      # 1) swap lesser_than_pointer and idx values
      list[idx], list[lesser_than_pointer] = list[lesser_than_pointer], list[idx]
      # 2) increment lesser_than_pointer
      lesser_than_pointer += 1
  # After the loop is finished...
  # swap pivot with value at lesser_than_pointer
  list[lesser_than_pointer], list[end] = list[end], list[lesser_than_pointer]
  print(list[start])
  start += 1
  return quicksort(list, start, end)

my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)