x = int(input("Enter a number: "))

org = x
rvr = 0

while x > 0:
    digit = x % 10
    rvr = rvr * 10 + digit
    x //= 10

if org == rvr:
    print(rvr, " is a palindrome")
else:
    print(org, " is not a palindrome")
