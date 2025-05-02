#Write a program to accept the cost of a bike and display the total cost after applying the following taxes:
'''
>100000 = 15% tax
>50000 and <= 100000 = 10% tax
<= 50000 = 5% tax
'''

x = int(input("Enter the cost of the bike: "))

if x > 100000:
    tax = 0.15 * x
    total_cost = x + tax
    print("Total cost after 15% tax: ", total_cost)
    print("Tax amount: ", tax)

elif x > 50000 and x <= 100000:
    tax = 0.10 * x
    total_cost = x + tax
    print("Total cost after 10% tax: ", total_cost)
    print("Tax amount: ", tax)
elif x <= 50000:
    tax = 0.05 * x
    total_cost = x + tax
    print("Total cost after 5% tax: ", total_cost)
    print("Tax amount: ", tax)
else:
    print("Invalid input")