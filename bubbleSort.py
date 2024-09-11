array = [32,12,11,100, 42,12,4,1, 0, 15 , 23 , 69] # 8 values

length = len(array) 

for outer_control in range(length - 1):
    for inner_control in range( outer_control - length - 1):
        if array[inner_control] > array[inner_control + 1]:
            array[inner_control], array[inner_control + 1] = array[inner_control + 1] , array[inner_control]

print("Sorted array: " , array )

    