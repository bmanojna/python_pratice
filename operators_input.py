# swap two numbers

a = 8
b = 9
print("before swapping a is",a,"and b is",b)
temp = a
a = b
b = temp
print("after swapping a is ",a,"and b is ",b)

# swaping two numbers without an temp variable
a = 2
b = 7
print("before swapping a is",a,"and b is",b)
a = a + b
b = a - b
a = a - b
print("after swapping a is ",a,"and b is ",b)

# swapping two numbers by using multiplication and division

a = 7
b = 5
print("before swapping a is",a,"and b is",b)
a = a * b
b = a/b
a = a/b
print("after swapping a is ",a,"and b is ",b)

# swap two numbers using bitwise operators

a = 9
b = 8
print("before swapping a is",a,"and b is",b)
a = a ^ b
b = a ^ b
a = a ^ b
print("after swapping a is ",a,"and b is ",b)

# find the area of of the circle

radius = 6
pi = 3.14
area = pi * radius * radius
print("area of the circle is",area)

# find the area of the reactangle

length = 89
breadth = 45
area = length * breadth
print("area of the rectangle is",area)
# find the area of the triangle

base = 78
height = 34
area = 1/2 * base * height
print("area of the triangle is",area)
# find the area of the square 
side = 6
area = side * side
print("area of the square is",area)

# area of the trapizum

a = 6
b = 9
h = 7
area = 0.5 * (a+b) * h
print("area of the trapizum is",area)

# find the simple interest calculator

prin = 100
rate = 6
time = 2
simple_interest = (prin * rate * time) / 100
print("the simple interest is",simple_interest)

# find the compound simple interest calculator

principle = 6000
rate = 5
time = 2
compound_interest = principle * (1+rate/100) ** time - principle
print("the compound interest is",compound_interest)

# find the percentage of a number

total_marks = 600
marks_obtained = 563
percentage = marks_obtained / total_marks * 100
print("percentage of a number is",percentage)

# find the mean of natural numbers

a = 8
b = 9
c = 8
d = 7
mean = (a+b+c+d) / 4
print("the mean of natural numbers is ",mean)

# find the median of natural numbers

a = 78
b = 56
c = 90
d = 89
e = 67
f = 90
numbers = [a,b,c,d,e,f]
numbers.sort()
n = len(numbers)
if n % 2 == 0:
	median = (numbers[n//2 - 1] + numbers[n//2]) / 2
	print("the median of the numbers is", median)
else:
	median = numbers[n//2]
	print("the median of the numbers is", median)
	
# finding the number even or odd
num1 = int(input("enter a number, num: "))
if num1 == 0:
	print("the number is zero")
elif num1 % 2 == 0:
	print("the number is even")
else:
	print("the number is odd")
   
