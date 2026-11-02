# sum of numbers up to value & factorial of a number

value = int(input("Enter a value: "))
value_factorial = value  # store the original value for factorial calculation
sum_of_numbers = 0

while value > 0:
    sum_of_numbers += value  # add the current value to the sum
    value -= 1  # decrement the value by 1

print(f"The sum of numbers up to the {value} is: {sum_of_numbers}")

factorial = 1
for i in range(1, value_factorial + 1):
    factorial *= i
print(f"The factorial of {value_factorial} is: {factorial}")