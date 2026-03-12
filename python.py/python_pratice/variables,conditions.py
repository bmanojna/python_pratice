
#Take two numbers and print the larger number.
num1=int(input("enter a num 1: "))
num2=int(input("enter a num 2: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("both numbers are equal")

#Take three numbers and print the largest number.
num1=int(input("enter a num 1: "))
num2=int(input("enter a num 2: "))
num3=int(input("enter a num 3: "))
if num1 > num2 and num1 > num3:
    print(num1,"numberone is greater",num2,num3)
elif num3>num1 and num3 >num2:
    print(num3,"numberthree is greater",num1,num2)
elif num2 > num1 and num2 > num3:
    print(num2,"numbertwo is greater",num1,num3)
else:
    print("all the numbers are equal")

#Take a number and check even or odd.
num=int(input("enter a number: "))
if num % 2 == 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

#Take a number and check positive, negative, or zero

key=int(input("enter a number: "))
if key > 0:
    print(key,"is a positive number",key)
elif key < 0:
    print(key,"is a negative number",key)
else:
    print(key,"is zero",key)

    # square of a number of a number
    num=(int(input("enter a number: ")))
    square = num**2
    print(num,"the square of number is",square)