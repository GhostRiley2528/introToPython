# Input marks for 5 subjects
print("*the marks entered are considered out of 100")
s1 = float(input("Enter marks for subject 1: "))
s2 = float(input("Enter marks for subject 2: "))
s3 = float(input("Enter marks for subject 3: "))
s4 = float(input("Enter marks for subject 4: "))
s5 = float(input("Enter marks for subject 5: "))

# Calculate percentage
percentage = (s1 + s2 + s3 + s4 + s5) / 5

# Print result
print("Percentage:", percentage, "%")
