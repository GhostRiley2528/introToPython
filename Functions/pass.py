def twist_fizz_buzz(start, end):
    for num in range(start, end+1):
        if num % 20 == 0:
            print("twist")
        elif num % 15 == 0:
            pass
        elif num % 5 == 0:
            print("fizz")
        elif num % 3 == 0:
            print("buzz")
        else:
            print(num)
print("Enter the start number: ")
start = int(input())
print("Enter the end number: ")
end = int(input())
twist_fizz_buzz(start, end)
