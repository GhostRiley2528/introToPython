def first_digit(n):
    while n >= 10:
        n = n // 10
    return int(n)

n = int(input("Enter a number: "))
print("The first digit is:", first_digit(n))
