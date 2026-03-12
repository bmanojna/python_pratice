# Print numbers from 1 to 100 using a loop

for i in range(1, 101):
    print(i)

# print even numbers from 1 to 100 using loop

for i in range(1,101):
    if i % 2 == 0:
        print(i)
# print odd numbers from 50 t0 100 using loop and size of the loop

for i in range(50,101):
    if i % 2 != 0:
        print(i)
size = len(range(50,101))
print("size of the loop is",size)

#print the multiplication table of a number using loop
num = 7
for i in range(1,21):
   mul = num * i
   print("7 *",i,"=",mul)
size = len(range(1,21))
print("size of the loop is",size)

# print the mutliplication of a number only even numbers using loop

num = 2
for i in range(1,6):
    if i % 2 == 0:
        mul = num * i
        print("2 *",i,"=",mul)


# print the sum of natural numbers
n=80
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("the sum of ",n,"numbers is",sum)

#finding the factorial of a number using loop
num = 5
fact = 1
for i in range(1, num + 1):
     fact = fact * i
print("the factorial of", num, "is", fact)