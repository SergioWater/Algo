

def quicksort(unsorted_sequence):
    length = len(unsorted_sequence)

    if length <= 1 :
        return unsorted_sequence
    else:
        #pop grabs the last index and returns it 
        pivot = unsorted_sequence.pop()


    items_greater = []
    
    items_lower = []

    for number in unsorted_sequence:
        if number > pivot:
            items_greater.append(number)
        else:
            items_lower.append(number)
    return  quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([-8, -1, 0, 1, 1, 1, 2, 2, 3, 5, 6, 10, 11, 12, 13, 13, 13, 53, 100, 122]))