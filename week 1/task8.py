DOB = input("Enter your date of birth (DD-MM-YYYY): ")

day, month, year = map(int, DOB.split('-'))

if month > 9 and day > 28:      #current date to see if the birthday has passed this year
    age = 2026 - year
else:
    age = 2025 - year

if day > 28: # check if the birthday has passed this month
    age_months = age * 12 + (month) 
else:
    age_months = age * 12 + (month - 1)

age_days = age * 365 + (month - 1) * 30 + day 


print(f"You are {age} years old.")
print(f"You are approximately {age_months} months old.")
print(f"You are approximately {age_days} days old. (excluding leap years)")
print(f"You were born on {year}-{month:02d}-{day:02d}.")


