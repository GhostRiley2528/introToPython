print("Choose on of the Rides (1/2):-")
print("1. Bike ")
print("2. Car \n")

c = int(input("Enter your choice : "))

if (c == 1):
    print("Great! Now choose one of the following (1/2):-")
    print("1. Scooter")
    print("2. Bike \n")
    c1 = int(input("Enter your choice : "))
    if (c1 == 1):
        print("Great! you have selected a Scooter")
    else:
        print("Great! You have selected a Bike!")

elif (c == 2):
    print("Great! now choose one of the following (1/2):-")
    print("1. SUV")
    print("2. XUV \n")
    c3 = int(input("Enter your choice : "))
    if (c3 == 1):
        print("Great! You selected an SUV!")
    else:
        print("Great! You have Selected an XUV!!")
    