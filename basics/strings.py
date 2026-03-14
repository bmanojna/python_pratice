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
x = ("manu")
word = ''.join(x)
palindrome = word == word[::-1]
print("the palindrome of x",x)

# count vowels
vowels = ("a","e","i","o","u")
size = len(vowels)
print("the size of vowels",size)

#remove spaces 
x = ("m ","n. ")
# Remove spaces from each string in the tuple and join them
removed = ''.join(s.replace(' ', '') for s in x)
print("after removing the spaces", removed)

