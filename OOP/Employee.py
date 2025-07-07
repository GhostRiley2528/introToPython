import time
class Employee:
    def __init__(self):
        print("Employee created ")
        time.sleep(2) 
    def __del__(self):
        print("Destrcutor called  ")
        time.sleep(2)
def create_and_delete_employee():
    print("Creating an employee object...")
    time.sleep(2)
    emp = Employee()  
    print("Employee object created...")
    time.sleep(2)
    print("Function ending...")
    del emp         

time.sleep(2)
create_and_delete_employee()