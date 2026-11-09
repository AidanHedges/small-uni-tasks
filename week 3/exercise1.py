# code to take score and generate grade
grades = True # variable to keep track of whether the score is valid or not
while grades == True: # loop to keep asking for score until a valid score is entered
    score = int(input("Enter your score (Or 101 to quit): "))

    if score == 101: # checks if score is 101, if it is then it is a quit signal
        grades = False
    elif score > 100 or score < 0: # checks if score is greater than 100 or less than 0, if it is then it is invalid
        print("Invalid score. Please enter a score between 0 and 100.")
    elif score >= 80: # checks if score is greater than or equal to 80, if it is then it is an A
        print(f"Your score of {score} is an A.")
    elif score >= 60: # checks if score is greater than or equal to 60, if it is then it is a B
        print(f"Your score of {score} is a B.")
    elif score >= 50: # checks if score is greater than or equal to 50, if it is then it is a C
        print(f"Your score of {score} is a C.")
    else: # if the score is not greater than or equal to 50, it must be an F    
        print(f"Your score of {score} is an F.")

