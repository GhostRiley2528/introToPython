x = int(input("enter number of rows: "))
x = x+1
for i in range(1, x, 1):
    for n in range(1, i +1):
        print(n , end=" ")
    print()