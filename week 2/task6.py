# collatz sequence

number = int(input("Enter a positive integer: "))
steps = 0

while number != 1:
    if number % 2 == 0:  # if the number is even
        number = number / 2
    else:  # if the number is odd
        number = (3 * number) + 1
    print(number)
    steps += 1

print(f"The number of steps to reach 1 is: {steps}")