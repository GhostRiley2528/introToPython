class person(object):
    def __init__ (self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)

class employee(person):
       def display(self, name, idnumber, salary , post):
        self.post = post
        self.salary = salary

        person.__init__(self,name, idnumber)

emp = employee("Arnav", 9393, 100000, "Intern")

emp.display()