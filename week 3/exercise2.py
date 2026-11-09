first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

def greet_user(first_name, last_name):
    full_name = f"{first_name.title()} {last_name.title()}"
    string = (f"Hello, {full_name}! Welcome!")
    return string

print(greet_user(first_name, last_name))
