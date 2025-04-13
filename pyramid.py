x = input("Enter a special character or a number to make a pyramid of it: ")
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i+1):
        print(x , end=" ")

    print()