x = input("please enter a word : ")
char = input("enter a character from the word: ")
i = 0
count = 0
while (i < len(x)):

    if(x[i] == char):
        count = count + 1
    i = i+1
print("The total number of times " , char , " has appeared is " , count , " times.")


string = input("Please enter your own word : ")

c = input("Please enter your own Character : ")
ii = 0
cc = 0

while(ii < len(string)): 

  if(string[ii] == c): 
    cc = cc + 1
  ii = ii + 1


print("The total Number of Times ", c, " has Occurred = " , cc)