class person(object):
    def __init__ (self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)

class employee(person):
       def display(self, name, idnumber, post , salary):
        self.post = post
        self.salary = salary

        person.__init__(self,name, idnumber)

emp = employee("Arnav", 9393, "Intern", 100000)

emp.display()