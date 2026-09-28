direction = input("Would you like to convert from Celsius -> Fahrenheit [C] or Fahrenheit -> Celsius [F]? ")
if direction.upper() == "C":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif direction.upper() == "F":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    