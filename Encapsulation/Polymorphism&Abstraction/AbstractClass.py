from abc import ABC, abstractmethod

class BaseClass(ABC):
    def display_value(self):
        print("This is a regular method in BaseClass.")

    @abstractmethod
    def abstract_method(self):
        pass

class DerivedClass(BaseClass):
    def abstract_method(self):
        print("This is the implemented abstract method in DerivedClass.")


obj = DerivedClass()
obj.display_value()
obj.abstract_method()
