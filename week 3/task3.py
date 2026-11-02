# numbers up to value, prints buzz, pop and buzzpop

value = int(input("Enter a value: "))

for i in range(1, value + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: BuzzPop")
    elif i % 3 == 0:
        print(f"{i}: Buzz")
    elif i % 5 == 0:
        print(f"{i}: Pop")
    else:
        print(i)

