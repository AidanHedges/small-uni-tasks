
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

procedure = input("Enter the operation (+, -, *, /): ")
if procedure == "+":
    result = num_1 + num_2
    print(f"The result of {num_1} + {num_2} is: {result}")

elif procedure == "-":
    result = num_1 - num_2
    print(f"The result of {num_1} - {num_2} is: {result}")

elif procedure == "*":
    result = num_1 * num_2
    print(f"The result of {num_1} * {num_2} is: {result}")

elif procedure == "/":
    if num_2 != 0:
        result = num_1 / num_2
        print(f"The result of {num_1} / {num_2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")


