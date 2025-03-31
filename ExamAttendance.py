med = input("Was there a medical cause? (Y/N)")
at = int(input("Enter your attendance."))

if (med == "Y"):
    print("You are allowed.")
else:
    print("You are not allowed.")