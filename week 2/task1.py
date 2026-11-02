# code to tell if a number inputted is odd

number = int(input("Enter a number: "))

if number % 2 == 0: # divides number and keeps remainder, if remainder is 0 then number is even
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

