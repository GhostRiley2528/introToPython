def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1,2,3,4): "))
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if choice == 1:
    print(add(x, y))
    exit()

elif choice == 2:
    print(subtract(x, y))
    exit()

elif choice == 3:
    print(multiply(x, y))
    exit()

elif choice == 4:
    print(divide(x, y))
    exit()
    
