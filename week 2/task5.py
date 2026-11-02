# sum of digits of a number

number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10  # get the last digit
    sum_of_digits += digit  # add the digit to the sum
    number //= 10  # remove the last digit from the number

print(f"The sum of digits of the number is: {sum_of_digits}")