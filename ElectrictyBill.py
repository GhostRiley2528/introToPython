unit = int(input("Please enter amount of Units consumed by user : "))

if (unit < 50 ):
    amnt = unit*2.60
    surcharge = 25
elif (unit <= 100):
    amnt = 130 + ((unit-50)* 3.25)

elif(unit <= 200):
    amnt = 130 + 162.50 + ((unit - 100) * 5.26)
    surcharge = 45
else:
    amnt = 130 + 162.50 + 526 + ((unit - 200) * 8.45)
    surcharge = 75
total = amnt + surcharge
print("Electricity bill = %.2f" %total)