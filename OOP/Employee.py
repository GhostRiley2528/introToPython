class Employee:
    def __init__(self):
        print("Employee created ")

    def __del__(self):
        print("Destrcutor called  ")

def create_and_delete_employee():
    print("Creating an employee object...")
    emp = Employee()  
    print("Employee object created...")
    print("Function ending...")
    del emp         


create_and_delete_employee()