
class Library:
    def __init__(self):      
        self.user_1 = None
        self.user_2 = None
        self.user_3 = None                  
        self.user_4 = None
        self.prompt=None
        self.Book1=None
        self.Book2=None
        self.Book3=None
        self.Book4=None

    def Users_Info(self):
        ID=""
        Name=""
        self.user_1 = {
            Name: "Maidah Chaudhary",
            ID: 123456,

        }
        self.user_2 = {
            Name: "Iqra Chaudhary",
            ID: 654321,            

        }
        self.user_2 = {
            Name: "Hira Noureen",
            ID: 750936,
        }
        self.user_2 = {
            Name: "Shahzad Hussain Chaudhary",
            ID: 210254,
        }
 
    def Books_Info(self):
        ID=""
        Title=""
        self.Book1 = {
            Title: "Harry Potter",
            ID: 890999,

        }
        self.Book2 = {
            Title: "Sponge Bob Square Pants",
            ID: 784446,            

        }
        self.Book3 = {
            Title: "Jurassic World",
            ID: 789456,
        }
        self.Book4 = {
            Title: "A Fish On A Tree",
            ID: 326598,
        }
    def taking_prompt(self):
        self.taking_prompt=input("Enter user ID : ")
        self.taking_prompt=input("Enter user Name : ")
        for elements in (self):



    
    
            
object1=Library()
print(object1.())

