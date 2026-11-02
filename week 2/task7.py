# fibonacci sequence

amount = int(input("Enter the amount of terms of the fibonacci sequence: "))

a = 1
b = 1

for i in range(amount):
    print(a)
    a, b = b, a + b
    
