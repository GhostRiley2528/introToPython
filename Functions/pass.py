def twist_fizz_buzz(start, end):
    for num in range(start, end+1):
        if num % 20 == 0:
            print("twist")
            break
        elif num % 15 == 0:
            pass
        elif num % 5 == 0:
            print("fizz")
            break
        elif num % 3 == 0:
            print("buzz")
            break