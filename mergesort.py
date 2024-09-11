
def mergesort(a, b,array):

    #sorted_list = []
    length_of_list_a = len(a)
    length_of_list_b = len(b)

    left_pointer = right_pointer = oringal_array_pointer = 0

    while left_pointer < length_of_list_a and right_pointer < length_of_list_b:
        if a[left_pointer] <= b[right_pointer]:
            array[oringal_array_pointer] = a[left_pointer]
            left_pointer += 1
        else:
            array[oringal_array_pointer] = b[right_pointer]
            right_pointer += 1
        oringal_array_pointer += 1
        
    while left_pointer < length_of_list_a:
            array[oringal_array_pointer] = a[left_pointer]
            left_pointer += 1
            oringal_array_pointer += 1

    while right_pointer < length_of_list_b:
            array[oringal_array_pointer] = b[right_pointer]
            right_pointer += 1
            oringal_array_pointer += 1
         

    return array

def breaksort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array)//2

    
    left = array[:mid]
    right = array[mid:]


    
    left = breaksort(left)
    right = breaksort(right)

    return mergesort(left,right,array)





if __name__ == '__main__':
     test_cases = [


        [100,90,81,53,62,44,21,10,5,0,-1],
        
     ]
     for tests in test_cases:
          breaksort(tests)
          print(tests)


