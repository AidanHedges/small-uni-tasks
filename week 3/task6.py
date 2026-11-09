# takes inputs, lists odd and even inpits and tally of each
taken_inputs = []
odd_inputs = []
even_inputs = []
take_input = True
while take_input:
    user_input = input("Enter a number (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        take_input = False
    else:
        try:
            number = int(user_input)
            taken_inputs.append(number)
            if number % 2 == 0:
                even_inputs.append(number)
            else:
                odd_inputs.append(number)
        except ValueError:
            print("Please enter a valid integer or 'done' to finish.")

print(f"you entered {len(taken_inputs)} numbers")
print(f"{len(even_inputs)} of them were even")
print(f"{len(odd_inputs)} of them were odd")
decision = input("Would you like to see the even and odd numbers? (yes/no): ")
if decision.lower() == 'yes':
    print(f"Even numbers: {even_inputs}")
    print(f"Odd numbers: {odd_inputs}")
