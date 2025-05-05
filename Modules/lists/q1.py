#Creat an empty list
# ask user for the number of elements in the list
# ask user for the elements in the list
#make two lists, one for even and one for odd numbers
# print the even and odd numbers in the list

L = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    L.append(int(input("Enter the elements in the list: ")))
print("The orignal list is:", L)
even = []
odd = []
for i in L:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
print("The even numbers in the list are: ", even )
print(" \n The odd numbers in the list are: ", odd)