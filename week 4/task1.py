#Exercise 1 - Shadow Copy Trap 
#-------------------------------- 
list_a = [5, 10, 15] 
list_b = list_a 
list_a[1] = 99 
print("list_a:", list_a) 
print("list_b:", list_b) 
 
#Predict the output, then explain why both lists changed. 
#Afterward, fix it so that list_b stays [5, 10, 15] even if list_a changes. 
# the first print will 