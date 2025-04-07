a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a >= b) and (a >= c):
    print(a, "is the largest of the three.")
elif (b >= a) and (b >= c):
    print(b, "is the largest of the three.")
else:
    print(c, "is the largest of the three.")

if (a == b) and (b == c):
    print("All three numbers are equal.")

str = input("\n Enter a word: ")
str0 = ('')
for i in str:
    str0 = i + str0
    print("The orignal String: ")
    print("\n Reversed String: ", str0, "\n")

def is_palindrome(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]

d = input("Enter a string: ")
if is_palindrome(d):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")