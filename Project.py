# ordering block
total=[]
menu_foods= print("""Select a food from the following: 
_____________________ Foods _____________________                 
1) Pizza  -- Rs.1800
2) Hamburger -- Rs.320
3) Zinger Burger -- Rs.250
4) Shawarma  --Rs.200
5) Loaded Fries --Rs.730
6) Nuggets  --Rs.120  """)

selected_foods=int(input("Input the selected food: "))
if selected_foods==1:
        bought_foods="Pizza"
        price_food=1800
        

elif selected_foods==2:
        bought_foods="Hamburger"
        price_food=320
    

elif selected_foods==3:
    bought_foods="Zinger Burger"
    price_food=250
    

elif selected_foods==4:
    bought_foods="Shawarma"
    price_food=250
    

elif selected_foods==5:
    bought_foods="Loaded Fries"
    price_food=730
    

elif selected_foods==6:
    bought_foods="Nuggets"
    price_food=120


elif selected_foods==7:
    bought_foods="Coke"
    price_food=450


elif selected_foods==8:
    bought_foods="Fanta"
    price_food=320


elif selected_foods==9:
    bought_foods="Sprite"
    price_food=320


elif selected_foods==10:
    bought_foods="Mango Juice"
    price_food=50


elif selected_foods==11:
    bought_foods="Orange Juice"
    price_food=50
how_many=int(input(f"Enter the quantity {bought_foods} : "))
food_total=how_many*price_food

menu_foods= print("""Select a food from the following: 
        _______ Drinks _______
1) Fanta -Rs.230
2) Coke -Rs.250
3) Sprite -Rs.210
4) Apple Juice -Rs.250           
5) Banana Milkshake -Rs.210
6) Chocolate Milkshake -Rs.210                """)
selected_drinks=int(input("Input the selected drinks: "))
if selected_drinks==1:
     bought_drinks="Fanta"
     drink_price=250
elif selected_drinks==2:
     bought_drinks="Coke"
     drink_price=250

elif selected_drinks==3:
     bought_drinks="Sprite"
     drink_price=210

elif selected_drinks==4:
     bought_drinks="Apple Juice"
     drink_price=250

elif selected_drinks==5:
     bought_drinks="Banana Milkshake"
     drink_price=210

elif selected_drinks==6:
          bought_drinks="Banana Milkshake"
          drink_price=210

how_many_drinks=int(input(f"Enter the quantity of {bought_drinks}:   "))
drink_total = drink_price * how_many


empty=[]
total.append(food_total)
total.append(drink_total)
for elements in total:
    empty.append(elements)
print("Your total is : Rs.",sum(empty))