def weather(c):
    if c > 30 :
        return "It's hot"
    elif c > 10 and c <= 30:
        return "It's mild"
    elif c > 0 and c <= 10:
        return "It's cold"
    else:
        return "Invalid input"
w = input("Enter temperature in Celsius: ")
print(weather(int(w)))