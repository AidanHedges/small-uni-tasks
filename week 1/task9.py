cart = []
shopping = True

while shopping == True:

    action = input("Would you like to add to the cart, remove an item from the cart, view the cart or checkout? (add/remove/view/checkout): ")
    if action.lower() == "add":
        item = input("Enter the item you would like to add to the cart: ")
        price = float(input(f"Enter the price of {item}: "))
        item_info = {"item": item, "price": price}
        cart.append(item_info)
        print(f"{item} has been added to the cart.")

    elif action.lower() == "remove":
        item = input("Enter the item you would like to remove from the cart: ")
        for i in range(len(cart)):
            if cart[i]["item"] == item:
                del cart[i]
                print(f"{item} has been removed from the cart.")
                break
        else:
            print(f"{item} is not in the cart.")

    elif action.lower() == "view":
        if len(cart) == 0:
            print("The cart is empty.")
        else:
            print("Items in the cart:")
            for item_info in cart:
                print(f"{item_info['item']}: ${item_info['price']}")

    elif action.lower() == "checkout":
        if len(cart) == 0:
            print("The cart is empty. Please add items to the cart before checking out.")
        else:
            total = sum(item_info["price"] for item_info in cart)
            print(f"The total cost of the items in the cart is: ${total}")
            print("Thank you for shopping with us!")
            shopping = False

