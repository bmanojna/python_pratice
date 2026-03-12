

#  data types
from math import sqrt
import math


a = 1
print(type(a))
b = 0.009
print(type(b))
m="nano"
print(type(m))

c = math.hypot(4, 3)
print(type(c))
d = math.sqrt(16)
print(type(d))

# convert celisus to fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) +32
print("the temperature in farenheit is",fahrenheit)

#find the square of a number
num = 5
square = num ** 2
print("the square of a number",num,"is",square)

# addition of two nummbers
num1 = (int(input("enter the first number: ")))
num2 = (int(input("enter the second number: ")))
sum = num1+num2
print("the sum of num1 and num2 is",sum)