class myClass:
    __privateVar = 10

    def __privMethod(self):
        print("This is a private method")

    def hello(self):
        print("Hello from myClass", myClass.__privateVar)
        
foo = myClass()
foo.hello()