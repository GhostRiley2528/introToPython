import random
p = True
num = str(random.randint(1, 20))
print("You have to guess the number i chose from 1 to 20")
print("You will win when you get the correct answer")
while p:
    x = int(input("Enter your guess: "))
    if x==num:
        print("You won!")
    else:
        print("Incorrect")
        print("Try again \n")