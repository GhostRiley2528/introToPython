class Compare3:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


ob1 = Compare3(3)
ob2 = Compare3(4)
ob3 = Compare3(3)


print("ob1 < ob2:", ob1 < ob2)    
print("ob1 == ob2:", ob1 == ob2)  
print("ob1 == ob3:", ob1 == ob3) 
