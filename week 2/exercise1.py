#Get input from a user, (check if it’s numeric)*, if the number is > 0, print the number and its square. If the number is 0, the program breaks out of the loop. For any other input the program prompts again​

while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)

        if number > 0:
            print(f"The number is {number} and its square is {number ** 2}")
        elif number == 0:
            print("The number is 0. Exiting the program.")
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
