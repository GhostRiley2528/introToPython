cp = float(input("Enter the Cost Price: "))
sp = float(input("Enter the Selling Price: "))

if sp>cp:
    sum = sp - cp
    print("The total Profit made is: " , sum)
else:
    print("No profit was made ")