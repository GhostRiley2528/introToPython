x = input("Enter a special character or a number to make a pyramid of it: ")
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i+1):
        print(x , end=" ")

    print()

f =int(input("Enter the number of rows:"))
num = 1
print("Floyd's Triangle")
for l in range(1, f, 1):
    for m in range(1, l+1):
        print(num , end=" ")
        num = num+1
    print()