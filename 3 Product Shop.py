Shopping_Cart=[]

#Creating Products
class MiniMart:
    def __init__(self):
        self.Product_1="Cheese"
        self.Product_2="Dough"
        self.Product_3="Pizza Sauce"
        Entry1=None
        Entry2=None
        Entry3=None
   
    def Details(self):
        Entry1=input(f"""Enter your first product from: 
                1) {self.Product_1}
                2) {self.Product_2}
                3) {self.Product_3} 
     >>> """)
        Entry2=input(f"""Enter your second product from: 
                1) {self.Product_1}
                2) {self.Product_2}
                3) {self.Product_3} 
     >>>  """)

        Shopping_Cart.append(Entry1)
        Shopping_Cart.append(Entry2)
        print("Your Cart: ",Shopping_Cart)
        Entry3=input(f"Which item would you like to remove from {Shopping_Cart}   :")
        Shopping_Cart.remove(Entry3)
        print("Your Cart: ",Shopping_Cart)
        for elements in Shopping_Cart:
            if elements=="Dough":
                print("Your Total is $7")
            if elements=="Pizza Sauce":
                    print("Your total is $12")
            if elements=="Cheese":
                    print("Your total is $21")
            
Shop1=MiniMart()
Shop1.Details()

