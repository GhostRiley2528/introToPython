x = (1 , 2 ,3 ,4 , 4 , 3 , 2 , 1)
print(x)
#check wether the tuple is palindrome or not using for loop
for i in range(len(x)//2):
    if x[i] != x[-i-1]:
        print("The tuple is not palindrome")
        break
    else:
        print("The tuple is palindrome")



'''if x == x[::-1]:
    print("The tuple is palindrome")
else:   
    print("The tuple is not palindrome")'''