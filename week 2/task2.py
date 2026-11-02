# can tell is a number is positive, negative or zero
number = int(input("Enter a number: "))
if number > 0: # checks if number is greater than 0, if it is then it is positive
    print(f"The number {number} is positive.")
elif number < 0: # checks if number is less than 0, if it is then it is negative
    print(f"The number {number} is negative.")
else: # if the number is not greater than 0 and not less than 0, it must be zero
    print(f"The number {number} is zero.")