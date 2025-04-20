print("Choose one of the following:")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
print("3. Convert Kelvin to Celsius")
choice = int(input("Enter your choice: "))

if choice == 1:
    x = float(input("Enter temperature in Celsius: "))
    y = (x * 9/5) + 32
    print("Temperature in Fahrenheit is: ", y)

elif choice == 2:
    x = float(input("Enter temperature in Fahrenheit: "))
    y = (x - 32) * 5/9
    print("Temperature in Celsius is: ", y)
elif choice == 3:
    x = float(input("Enter temperature in Kelvin: "))
    y = x - 273.15
    print("Temperature in Celsius is: ", y)
else:
    print("Invalid choice!")