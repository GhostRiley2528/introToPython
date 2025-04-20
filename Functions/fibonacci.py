n = int(input("Choose the nth term for the Fibonacci series: "))

a = 0
b = 1
count = 0

print("Fibonacci Series:")
print(a, end=" ")
if n > 1:
    print(b, end=" ")

    for i in range(2, n):
        d = a + b
        print(d, end=" ")
        a = b
        b = d
