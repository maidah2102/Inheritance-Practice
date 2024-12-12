# Class on Student Info
class Student:
    def __init__(self):
        self.name=None
        self.roll_number=None

    def input_info(self):
        self.name=input("Enter you name: ")
        self.roll_number=input("Enter you roll-number: ")
    def display_info(self):
        return (f"Your name is {self.name} and your roll-number is {self.roll_number}")
object1=Student()
object1.input_info()
print(object1.display_info())
 
