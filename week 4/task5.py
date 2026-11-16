#Exercise 5 - Remove Duplicates Without Sets 
#------------------------------------------------- 
numbers = [4, 7, 4, 2, 9, 7, 2, 1, 4] 
#Write a program that builds a new list with unique values in the same order they first appear. 
#Expected output: [4, 7, 2, 9, 1] 

numbers_unique = []
for i in numbers:
    print(i)
    if i in numbers_unique:
        print("not unique")
        
    else:
        numbers_unique.append(i)
    
print(numbers_unique)