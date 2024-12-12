class Library:
    def _init_(self):
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
    def Issue_Return(self):
        self.prompt=input("Would You like to Return or Issue a book (I/R):  ")
        if self.prompt.lower()=="i":
            input("Enter Users ID: ")
            input("Enter users name: ")
            self.Book1={"Book1":"Harry Potter","ID":1202,}
            self.Book2={"Book2":"Sponge Bob","ID":5401,}
            self.Book3={"Book3":"Harry Potter","ID":1202,}
            self.Book4={"Book4":"Harry Potter","ID":1202,}
            input(f"""Which book would you like to issue:
                  1. {self.Book1}
                  2. {self.Book2}
                  3. {self.Book3}
                  4. {self.Book4}

                    """)
            
object1=Library()
print(object1.Issue_Return())