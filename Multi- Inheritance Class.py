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
object1.name="Hanna"
object1.age=21
object1.id="4512"
object1.details()
