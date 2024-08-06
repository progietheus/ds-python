# lists are internally implemented as arrays
# Accessing element - O(1) constant time complexity to access


#-1 last index
a =[1,2,3]
print("Last Index is " + str(a[-1]))


#Subarray slicing indices are left-inclusive and right-exclusive. For example,
a = [0, 10, 20, 30, 40, 50]
subarray = a[2:5]  # element from index 2 to index 4 (cuz right exclusive, 5-1=4)
# subarray = [20, 30, 40]

print("Subarry slice result (element from index 2 to index 4 (cuz right exclusive, 5-1=4)): " + str(subarray))

#There's also a shorthand for slicing from element 0. For example:
a = [0, 10, 20, 30, 40, 50]
subarray = a[:2]
# subarray = [0, 10]

print("Sub array slice result with shorthand from beginning: " + str(subarray))

#and slicing to the end,

a = [0, 10, 20, 30, 40, 50]
subarray = a[2:]
# subarray = [20, 30, 40, 50]


print("Sub array slice result with shorthand to end: " + str(subarray))

#In general, to iterate through a list, for loop is easier to reason than while since there's no condition to manage that could skip elements. You can also use enumerate to get both the index and element at the same time.
nums = [0, 10, 20, 30, 40, 50]
for i, num in enumerate(nums):
    print(i, num)
