DOB = input("Enter your date of birth (DD-MM-YYYY): ")
Current_date = input("Enter the currnet date (DD-MM-YYYY): ")

current_day, current_month, current_year = map(int, Current_date.split('-'))
day, month, year = map(int, DOB.split('-'))

if month > 9 and day > 28:      #current date to see if the birthday has passed this year
    age = current_year - year
else:
    age = current_year - year

if day > 28: # check if the birthday has passed this month
    age_months = age * 12 + (current_month-9) 
else:
    age_months = age * 12 + (current_month - 10)

age_days = age * 365 + (month - 10) * 30 + day 


print(f"You are {age} years old.")
print(f"You are approximately {age_months} months old.")
print(f"You are approximately {age_days} days old. (excluding leap years)")
print(f"You were born on {year}-{month:02d}-{day:02d}.")


