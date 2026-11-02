# takes 2 values, prints the prime numbers between

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
primes = []
if value1 > value2:
    value1, value2 = value2, value1  # swap values if value1 is greater than value2

for number in range(value1, value2 + 1):
    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        primes.append(number)

print(f"the prime numbers between {value1} and {value2} are: {primes}")