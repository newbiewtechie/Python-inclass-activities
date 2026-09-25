import array as  arr
array_num = arr.array('i', [1, 2, 3, 4, 7, 5 , 7, 9, 8, 7])
print("Original Array: ", array_num)
print("Number of occurences of the number 7  in the given array : " +str(array_num.count(7)))
array_num.reverse()
print("reverse the order of the itmes :", array_num)
