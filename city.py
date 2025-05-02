def print_monument():
    r = "Red Fort" 
    t = "Taj Mahal"
    j = "Jal Mahal"
    
    print("1. Delhi \n2. Agra \n3. Jaipur") 
    x = input("Choose a number to see the monument: ")
    
    if x == "1":
        print(r)
    elif x == "2":
        print(t)
    elif x == "3":
        print(j)
    else:
        print("Invalid choice")

# Main loop to call the function multiple times
while True:
    print_monument()
    choice = input("Do you want to choose again? (y/n): ")
    if choice.lower() != 'y':
        print("Exiting the program.")
        break
