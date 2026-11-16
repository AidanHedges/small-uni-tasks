#Exercise 1 - Shadow Copy Trap 
#-------------------------------- 
list_a = [5, 10, 15] 
#list_b = list_a 
list_b = list_a.copy()
list_a[1] = 99 
print("list_a:", list_a) 
print("list_b:", list_b) 
 
#Predict the output, then explain why both lists changed. 
#Afterward, fix it so that list_b stays [5, 10, 15] even if list_a changes. 

# the first print will be "list a: 5, 99, 15" as list_a[1] is the second term and is changed to 99
# list be will also print that as it is another refernace to list_a

# adding .copy() to the end creates list b as a copy of list a that is its own variable, and wont change with list a
