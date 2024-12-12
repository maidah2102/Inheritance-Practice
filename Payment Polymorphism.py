# polymorphism

class payment_method:
    def process_payment(self,amount):
        raise NotImplementedError("subclass must implement the functionality, not parent class")

class credit_card(payment_method):
    def process_payment(self,amount):

        print(f"processing credit card payment of ${amount}. ")

class paypal(payment_method):
    def process_payment(self,amount):
        print(f"processing paypal payment of ${amount}. ")
        
class bank_transfer(payment_method):
    def process_payment(self,amount):

        print(f"Processing bank transfer payment of ${amount}... ")

# polymorphism in action
def completepayment():
    payment_method1 = int(input("""Choose a payment method:
  1) Credit Card
  2) PayPal
  3) Bank Transfer
>>> """))
    # print("choose a payment method")
    # print("1. credit card")
    # print("2. paypal")
    # print("3. bank_transfer")

    # choice= int(input("enter your any choice"))
    amount= float(input("Enter your amount: "))
    if payment_method1 == 1:
        payment_method= credit_card()
    elif payment_method1 == 2:
        payment_method=paypal()
    elif payment_method1==3:
        payment_method=bank_transfer()
    else:
        print("Invalid choice.")
        

# process payment method   
    payment_method.process_payment(amount)
    # except ValueError:
    #     print("invalid input")


# 
    
completepayment()
