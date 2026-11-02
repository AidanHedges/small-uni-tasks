# fibonacci sequence

amount = int(input("Enter the amount of terms of the fibonacci sequence: "))
num1 = int(input("Enter the first number of the fibonacci sequence: "))
num2 = int(input("Enter the second number of the fibonacci sequence: "))

for i in range(amount):
    print(num1)
    num1, num2 = num2, num1 + num2

