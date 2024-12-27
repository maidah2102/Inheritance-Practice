more_foods="yes"
# List containing food
foods=[]
foods_name=[]
drinks=[]
quantity_foods_list=[]
# Lists containing all prices of selected foods
subtotal=[]
#while loop
while more_foods=="yes":
        foods_menu = """Select a food from the following:  
                1-  Pizza Cheesy 
                2-  Chicken Fajita Pizza
                3-  Veggie Pizza
                4-  French Fries
                5-  Crunchy Pasta
                6-  Macaroni
                7-  Nuggets
                8-  Shawarma
                9-  Zinger Burger
                10- Double Decker """
        print(foods_menu)
        selection_foods=int((input("Select a food from the menu above: ")))
        foods.append(selection_foods)
        quantity_foods= int(input(f"Enter the quantity of the selected food: "))
        quantity_foods_list.append(quantity_foods)
        more_foods=input("Would you like to select more foods? ")
# above are all variables needing user input

# statments containing price of selected food
        for elements in foods:
                if elements==1:  #pizza cheesy selection
                        price=1850*quantity_foods
                        food_name="Cheese Pizza"
                        subtotal.append(price)
                        foods_name.append(foods_name)

                elif elements==2: #pizza fajita selection
                        price=1870*quantity_foods
                        food_name="Chicken Fajita Pizza"
                        subtotal.append(price)
                        foods_name.append(foods_name)
                
                elif elements==3: #pizza veggie selection
                        price=1880*quantity_foods
                        food_name="Veggie Pizza"
                        subtotal.append(price)
                        foods_name.append(foods_name)
 

                elif elements==4: #french fries selection
                        price=420*quantity_foods
                        food_name="French Fries"
                        subtotal.append(price)
                        foods_name.append(foods_name)


                elif elements==5: #crunchy pasta selection
                        price=530*quantity_foods
                        food_name="Crunchy Pasta"
                        subtotal.append(price)
                        foods_name.append(foods_name)


                elif elements==6:    #macaroni selection
                        price=790*quantity_foods
                        food_name="Macaroni"
                        subtotal.append(price) 
                        foods_name.append(foods_name)


                
                elif elements==7:    #nuggets selection
                        price=320*quantity_foods
                        food_name="Nuggets"
                        subtotal.append(price) 
                        foods_name.append(foods_name)

                
                elif elements==8:    #shawarma selection
                        price=120*quantity_foods
                        food_name="Chicken Shawarma"
                        subtotal.append(price) 
                        foods_name.append(foods_name)

                

                elif elements==9:    #zinger burger selection
                        price=250*quantity_foods
                        food_name="Zinger Burger"
                        subtotal.append(price) 
                        foods_name.append(foods_name)



                elif elements==10:    #macaroni selection
                        price=550*quantity_foods
                        food_name="Double Decker"
                        subtotal.append(price) 
                        foods_name.append(foods_name)


else:
        more_drinks="yes"
take_drinks="no"
while more_drinks=="yes":
        while take_drinks!="yes":
                take_drinks=input("Would you like to select some drinks? no/yes : ")
                if take_drinks=="no":
                        print("-------Receipt---------")
                        for names in foods_name:
                                        for objects in foods:
                                                objects
                                        print(f"""Food Number {objects} : {price/quantity_foods} x {quantity_foods}""")
                                        print("--------Sub-total---------")
                                        print("Your total: Rs",sum(subtotal))
                        
        else:
                drinks_menu="""Select a food from the following: 
                        1-  Pepsi 250ml
                        2-  Coke  250ml
                        3-  Marinda 250ml
                        4-  Mango Juice
                        5-  Apple Juice
                        6-  Banana Milkshake
                        7-  Mango Milkshake
                        8-  Ice Cream Sundae
                        9-  Chocolate Blizard
                        10- Apple Orange Mix"""
                print(drinks_menu)
                selection_drinks=int(input("Enter the drink you would like: "))
                drinks.append(selection_drinks)
                quantity_drinks= int(input(f"Enter the quantity of your selected drink : "))

                more_drinks=input("Would you like to select more drinks? ")
                        

                for items in drinks:
                                if items==1:
                                        drink_price=50*quantity_drinks
                                        drink_name="Pepsi"
                                        subtotal.append(drink_price)

                                elif items==2:
                                        drink_price=60*quantity_drinks
                                        drink_name="Coke"
                                        subtotal.append(drink_price)

                                elif items==3:
                                        drink_price=60*quantity_drinks
                                        drink_name="Marinda"
                                        subtotal.append(drink_price)


                                elif items==4:
                                        drink_price=70*quantity_drinks
                                        drink_name="Mango Juice"
                                        subtotal.append(drink_price)



                                elif items==5:
                                        drink_price=70*quantity_drinks
                                        drink_name="Apple Juice"
                                        subtotal.append(drink_price)


                                elif items==6:
                                        drink_price=120*quantity_drinks
                                        drink_name="Banana Milkshake"
                                        subtotal.append(drink_price)


                                elif items==7:
                                        drink_price=120*quantity_drinks
                                        drink_name="Mango Milkshake"
                                        subtotal.append(drink_price)

                                elif items==8:
                                        drink_price=320*quantity_drinks
                                        drink_name="Ice Cream Sundae"
                                        subtotal.append(drink_price)

                                elif items==9:
                                        drink_price=170*quantity_drinks
                                        drink_name="Chocolate Blizard"
                                        subtotal.append(drink_price)


                                elif items==10:
                                        drink_price=130*quantity_drinks
                                        drink_name="Apple Orange Mix Fruit-Punch"
                                        subtotal.append(drink_price)
                                
                else:
                        print("----Reciept-----")

for objects in foods:
                        print(f"""Food Number {objects} : Rs.{price/quantity_foods} x {quantity_foods}""")
for liquid in drinks:
        print(f"""Drink Number {liquid} : Rs.{drink_price/quantity_drinks} x {quantity_drinks}""")

print("--------Bill---------")
print("Your Total: Rs.",sum(subtotal))