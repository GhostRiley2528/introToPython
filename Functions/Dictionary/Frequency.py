test = {'Codingal' : 1, 'is': 5, 'fun': 9, 'and': 4, 'I': 3, 'happiness': 1, 'it': 2, 'is': 5, 'great': 1}
print("The original dictionary is : " + str(test))
K = int(input("Enter the frequency to check: "))
res = 0
for key in test:
    if test[key] == K:
        res += 1
print("The frequency of K is : " + str(res))