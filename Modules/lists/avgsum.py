#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list. with random numbers by importing random
import random
List = []
for i in range(10):
    List.append(random.randint(1, 100))
print(" the orignal List is : ", List)
sum = 0
for i in List:
    sum += i
print("Sum: ", sum)
average = sum / len(List)
print("Average: ", average)
largest = max(List)
print("Largest: ", largest)
smallest = min(List)
print("Smallest: ", smallest)