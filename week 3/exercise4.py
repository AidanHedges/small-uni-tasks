#Write a function that accepts a string and counts the number of upper and lower case letters.​

string = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
for i in string:
    if i.isupper():
        uppercase_count += 1
    elif i.islower():
        lowercase_count += 1

print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")