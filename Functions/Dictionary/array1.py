import array as arr

x = arr.array('i', [1,2,3,4,5,1,1,4,5,7,9])
print("Original array:", x)
print("Number of occurrences of 1:", x.count(1))
print("Number of occurrences of 2:", x.count(2))
print("Number of occurrences of 3:", x.count(3))

x.reverse()
print("Reversed array:", str(x))
