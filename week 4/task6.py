#Exercise 6 - Function to Find Max 
#---------------------------------------- 
#Write a function find_max(lst) that returns the largest number in a list without using max(). 
 
#Example: 
#print(find_max([3, 8, 2, 5, 10, 4]))  # should print 10 

list = [3, 8, 2, 5, 10, 4]
def find_max(list):
    greatest = 0
    for i in list:
        print(i)
        if i > greatest:
            greatest = i
            print("replaced")
        
        else:
            print("Lower")
    
    return greatest

print(find_max(list))