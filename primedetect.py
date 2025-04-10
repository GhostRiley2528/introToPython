up = int(input("Enter the maximum range: "))
dn = int(input("Enter the minimum range: "))
print("The prime numbers between ", up , " and ", dn, " are: ")

for i in range (dn, up, 1):
    if i > 1:
        for num in range(2,i):
            if (i % num) == 0:
               break
        else:
            print(i, end=", ")