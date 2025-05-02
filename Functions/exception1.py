def a():
    try:
        x , y = eval(input("Enter two numbers separated by comma: "))
        result = x / y
        print("The result is: ", result)

    except ZeroDivisionError:
        print("Exception occurred, division by zero is not allowed.")

    except SyntaxError :
        print("Exception occurred, invalid syntax. (e.g., missing a comma or extra characters)")

    except:
        print("An unexpected error occurred.")
    else:
        print("No exceptions occurred.")

a()
i = int(input("enter 1 to try again "))
if i == 1:
    a()
else:
    print("exiting")