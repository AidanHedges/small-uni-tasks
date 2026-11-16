#Exercise 3 - Selective Deletion 
#------------------------------------- 
#Given: 
data = [10, 20, 30, 40, 50, 60, 70, 80] 
 
#1. Use del to remove the middle two elements. 
#2. Use del again to remove the first element. 
#3. Use del data[:] to empty the entire list. 
 
#Explain the difference between del data[:] and del data.

data1 = data.copy()
del data1[3:5]
print(data1)

data2 = data.copy()
del data2[0]
print(data2)

data3 = data.copy()
del data3[:]
print(data3)
del data3
# print(data3) - caues error as list no longer exists
# using del data[:] removes all the variables inside the list but retians the list
# printing this will print an empty array
# using del will delete the array and all its contents, after this the array data3 doesnt 
# exist, so cannot be printed or added to