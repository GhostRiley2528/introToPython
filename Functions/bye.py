x = False
while not x:
    try:
        n = int(input("Enter a number: "))
        while n % 2 == 0:
            print("bye")
            x = True
    except ValueError:
        print("Invalid")
/