class Person:
    name=""
    age=0
    id=""
    def details(self):
        print("These are the details of the employee: ")
class Employee(Person):
    def details(self):
        super().details()
        print(f"""Name: {self.name}
Age: {self.age}
ID: {self.id}
""")
object1=Employee()
object1.name=input("Enter the name of the employee: ")
object1.age=input("Enter the age of the employee: ")
object1.id=input("Enter the ID of the employee: ")
object1.details()
