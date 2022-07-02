Vector = list[int] #Will be used as a type hint for a list containing ints

def binary_search(list: Vector, item: int) -> (int | None):
    #low and high keep track of which part of the list will be searched; high needs to be divisable by 2 or handled
    low = 0
    high = len(list) - 1

    #While the target item has not be narrowed down keep searching
    while low <= high:
        #Set the middle element and guess; mid needs to be an int to be used as an index
        mid = int((low + high) / 2)
        guess = list[mid]

        #When the item is found return the index
        if guess == item:
            print("found solution")
            return mid
        
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    #Return None if no element was found
    return None

################ Demo ##########################################
test_list = [1,9,22,145,142,2222,425,3222,4,2]
#binary search can only work with a sorted list; so sort it
test_list.sort()
print(binary_search(test_list, 145))
################################################################
