#Exercise 7 - Copy by Slicing Function 
#---------------------------------------------- 
#Write a function copy_list(original) that: 
#1. Uses slicing ([:]) to create a copy. 
#2. Returns the copy. 
#3. Demonstrates that changes to the copy don’t affect the original. 
 
#Example: 
#nums = [1, 2, 3] 
#new_nums = copy_list(nums) 
#new_nums[0] = 99 
#print(nums)      # [1, 2, 3] 
#print(new_nums)  # [99, 2, 3] 

def copy_list(original):
    new_list = original[:]
    return new_list

list = [1, 2, 3]
new_list = copy_list(list)
new_list[0] = 99

print(list)      # [1, 2, 3]
print(new_list)  # [99, 2, 3]