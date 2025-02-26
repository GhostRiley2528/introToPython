amount = int(input("Enter the amount to withdraw" ))
#
note100 = amount//100
note10 = (amount%100) //50
note1 = ((amount%100)%50) //10
#
print("Notes of 100: ",note100,  "Notes of 10: ", note10, "Notes of 1: ", note1)