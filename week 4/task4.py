#Exercise 4 - Membership Check Practice 
#--------------------------------------------- 
#Given: 
inventory = ["pickaxe", "sword", "bow", "pork choppor"] 
 
#1. Ask the user for a fruit name. 
#2. If it’s in the list, print "Available!", otherwise print "Out of stock." 
#3. Extend the program to keep asking until the user types "exit". 
 
inventory_search = True
while inventory_search == True:

    wanted_fruit = input("What fruit would you like [enter 'exit' to close]: ").lower()
    
    
    if wanted_fruit in inventory:
        print("Available")
    elif wanted_fruit == "exit":
        inventory_search = False
    else:
        print("Out of stock")