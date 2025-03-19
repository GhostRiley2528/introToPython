print("Enter a number (Numerator) ")
num = int(input())
print("enter a number (Denominator)")
num1 = int(input())

if num % num1 == 0:
    print("\n" + str(num)+ "is divisble by "+str(num1))
else:
    print("\n" + str(num)+ "is not divisble by "+str(num1))
