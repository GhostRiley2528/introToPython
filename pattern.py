'''x = int(input("enter number of rows: "))
x = x+1
for i in range(1, x, 1):
    for n in range(1, i +1):
        print(n , end=" ")
    print()'''

l = int(input("enter number of rows: "))


for f in range(1, l, 1):
    for space in range(l - f):
        print(" ", end = " " )
    num = 1
    for j in range(2* f - 1):
        print(num, end=" ")
    print()