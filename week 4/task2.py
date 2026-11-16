#Exercise 2 - Working with Negative Slices 
#----------------------------------------------- 
#Given: 
values = [3, 6, 9, 12, 15, 18, 21] 
 
#Do the following using slices: 
#1. Create a list with the last 3 elements only. 
#2. Create a list that excludes the first and last elements. 
#3. Reverse the list using slicing. 

values1 = values[-3:]
print(values1)

values2 = values[1:-1]
print(values2)

values3 = values[::-1]
print(values3)