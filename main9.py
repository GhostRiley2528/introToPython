import math

# Input 
r = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
area = math.pi * r * r
perimeter = 2 * math.pi * r

#result
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
