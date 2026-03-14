
# to find list of numbers in a list
num1 = [1,2,3,4,5,6,7,89]
size = len(num1)
print("the size", size)

# the sum of elements in a list
x = [1,2,3,4]
sum = (1+2+3+4)
print("the sum of numbers in a list", sum)

#  find the largest element in a list
x = [5,6,7,8]
max_elem = max(x)
print("the largest element in a list:", max_elem)
x_sorted = sorted(x, reverse=True)
if len(x_sorted) > 1:
    print("the second largest element:", x_sorted[1])
if len(x_sorted) > 2:
    print("the third largest element:", x_sorted[2])

# the sum of elements in a list
x = [12,34,56]
sum = (12+34+56)
print("the sum of elements in a list",sum)

# the second largest element in a list
x = [30,31,32]
max_val = max(x)
x_sorted = sorted(x, reverse=True)
if len(x_sorted) > 1:
    print("the second largest element in the list:", x_sorted[1])

# remove duplicates
x = [34,67,89,67]
duplicates = list(set(x))
print("List after removing duplicates:", duplicates)

# remove duplicates
x = [90,91,92,93,91]
duplicates = list(set(x))
print("list after removing a duplicates in a list",duplicates)

# the smallest element in the list
x = [29,30,28,27]
min_value = min(x)
x_sorted = sorted(x)
if len(x_sorted) > 0:
    print("the first smallest element", x_sorted[0])
if len(x_sorted) > 1:
    print("the second smallest element", x_sorted[1])


