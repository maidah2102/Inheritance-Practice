# Excercise #1 Book in library
#Creating Class
class Books():
    #Initializing Variables
    def __init__(self):
        self.Book1=None
        self.title1=None
        self.avalibility1=None
        self.date_of_borrow1=None
        self.Book2=None
        self.title2=None
        self.avalibility2=None
        self.date_of_borrow2=None
        self.Book3=None
        self.title3=None
        self.avalibility3=None
        self.date_of_borrow3=None
        self.borrow_attempt=None
        self.return1=None
        self.return2=None
        self.return3=None
#Details of Book
    #Taqking Details From user (3 Books)
    def taking_details(self):
        self.Book1=print("--------------Book #1-------------------")
        self.title1=input("Enter the title of your first book: ")
        self.avalibility1=input("Has this book been borrowed (available)/(not available) : ")
        self.date_of_borrow1=input("At what date was it borrowed:  ")
        self.return1=input("At what date will you return this book? :  ")
        self.Book2=print("--------------Book #2-------------------")
        self.title2=input("Enter the title of your second book: ")
        self.avalibility2=input("Has this book been borrowed (available)/(not available) : ")
        self.date_of_borrow2=input("At what date was it borrowed:  ")
        self.return2=input("At what date will you return this book? :  ")
        self.Book3=print("--------------Book #3-------------------")
        self.title3=input("Enter the title of your third book: ")
        self.avalibility3=self.avalibility1=input("Has this book been borrowed (available)/(not available) : ")
        self.date_of_borrow3=self.date_of_borrow1=input("At what date was it borrowed: ")
        self.return3=input("At what date will you return this book? :  ")
#Displaying Info Based on prompt

    def displaying_info(self):
        self.borrow_attempt=input("Which book would you like to borrow: ")
        if self.borrow_attempt == "Book 1":
            return (f"""Book #1 is titled {self.title1} it is {self.avalibility1} at the library its date of borrow is {self.date_of_borrow1} the return of this book will be {self.return1} """)
        elif self.borrow_attempt=="Book 2":
            return (f"""Book #2 is titled {self.title2} it is {self.avalibility2} at the library its date of borrow is {self.date_of_borrow2} its return will be on {self.return2} """)
        elif self.borrow_attempt=="Book 3":
            return (f"""Book #3 is titled {self.title3} it is {self.avalibility3} at the library its date of borrow is {self.date_of_borrow3} the return of this book will be {self.return3}""")


object1=Books()
object1.taking_details()
print(object1.displaying_info())