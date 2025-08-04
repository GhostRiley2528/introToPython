#1: create a multiplication table for any given number till any given number
def mt(number, limit):
    print(f"\nMultiplication Table for {number} up to {limit}:\n")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage:
num = int(input("Enter the number to generate its table: "))
upto = int(input("Enter the limit: "))
mt(num, upto)

#2:  