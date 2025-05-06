#create and empty tuple
#create a tuple with 8 integers
#acces the 5th element of the tuple
#acces the 2nd to 5th elements of the tuple
#create another tuple and ask user to enter 5 elements one by one using for loop
#take the input from the user and append it to the tuple 
#display the tuple

x = ()
x1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(x1)
print("The 5th element of the tuple is: ", x1[4])
print("The 2nd to 5th elements of the tuple are: ", x1[1:5])
x2 = ()
inter = int(input("Enter the number of elements in the tuple: "))
for i in range(inter):
    x2 = x2 + (int(input("Enter the element: ")), )
print("The tuple is: ", x2)