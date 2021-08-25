import time

#Alright students! Here is the assignment
# part 1
#Step 1: make a wallet containing $100
#Step 2: make a menu - four items
#Step 2: ask user for things on the menu
#Step 3: display remaining balance in wallet

wallet = 100
print("You have $%s in your wallet \n \n" % wallet)
time.sleep(2)
custName = input("Hello I'm Kayla and welcome to my cottage! \nWhat is your name?   ")
print("Nice to meet you %s! Here is our menu" % custName)
time.sleep(2)
print(""" -------------------------- \n WELCOME TO KAYLA'S COTTAGE \n
        Menu Options:
        1. Hamburger Combo - $12.95
        2. Hot Dog Combo - $8.95
        3. Ice Cream Sundae - $7.95
        4. Famous Arnold Palmer - $2.95
        
 -------------------------- """)
time.sleep(2)
hamburger = 12.95
hotDog = 8.95
iceCream = 7.95
drink = 2.95
custOrder = int(input("Enter the item number of the item you would like: "))
if custOrder == 1:
    print("Hamburgr Combo comming right up!")
    wallet -= hamburger
    time.sleep(2)
    print("sizzle sizzle sizzle")
    time.sleep(1)
    print("bang bang")
    time.sleep(1)
    print("Pop!")
    time.sleep(2)
    print("Here is your order! Thank you and come again! \nYou are leaving the resturant with $%s" % wallet)
elif custOrder == 2:
    print("Hot Dog Combo comming right up!")
    wallet -= hotDog
    time.sleep(2)
    print("sizzle sizzle sizzle")
    time.sleep(1)
    print("bang bang")
    time.sleep(1)
    print("Pop!")
    time.sleep(2)
    print("Here is your order! Thank you and come again! \nYou are leaving the resturant with $%s" % wallet)
elif custOrder == 3:
    print("Yummy! Chocolate Drizzled Ice Cream Time!!")
    wallet -= iceCream
    time.sleep(2)
    print("sizzle sizzle sizzle")
    time.sleep(1)
    print("bang bang")
    time.sleep(1)
    print("Pop!")
    time.sleep(2)
    print("Here is your order! Thank you and come again! \nYou are leaving the resturant with $%s" % wallet)
elif custOrder == 4:
    print("We are famous for our Arnold Palmer! You will slap yo mama for it!")
    wallet -= drink
    print.sleep(2)
    print("sizzle sizzle sizzle")
    print.sleep(1)
    print("bang bang")
    print.sleep(1)
    print("Pop!")
    time.sleep(2)
    print("Here is your order! Thank you and come again! \nYou are leaving the resturant with $%s" % wallet)
else:
    print("That doesn't seem to be a menu option. I don't like my time being wasted! Bye")




