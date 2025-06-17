n1 = [1,2,3,4]
n2 = [5,6,7,8]
result = list(map(lambda x, y: x + y, n1, n2))
print(list(result))

nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("Square of numbers in list:",square)