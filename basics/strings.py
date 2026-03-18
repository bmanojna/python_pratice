#printing out the letters
x = ("a,b,c,d,e,f")
print("the letters",x)
x = ("manu","mano","madhu")
print("x")

# reverse string
X = "manojna"
reversed_x = ''.join(sorted(X, reverse=True))
print("the reverse string", reversed_x)

# longest reverse string 
Y = ("heyeveryonegoodtoseeyou")
reversed_Y = ''.join(sorted(Y, reverse=True))
print("the reversed string",reversed_Y)

# palindrome check
text = input("enter a text").lower
if text == text[::-1]
   print("it is an palindrome")
else :
   print("it is not a palindrome")
# count vowels
vowels = ("a","e","i","o","u")
size = len(vowels)
print("the size of vowels",size)

#remove spaces 
x = ("m ","n. ")
# Remove spaces from each string in the tuple and join them
removed = ''.join(s.replace(' ', '') for s in x)
print("after removing the spaces", removed)

