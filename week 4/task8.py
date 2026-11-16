#Exercise 8 - Delete Range Function 
#------------------------------------------- 
#Write a function delete_range(lst, start, end) that deletes a slice of elements between start and end indices. 
 
#Example: 
#data = [0, 1, 2, 3, 4, 5, 6, 7] 
#delete_range(data, 2, 5) 
#print(data) 
#Expected output: [0, 1, 5, 6, 7]

def delete_data_range(data, front, end):
    new_data = data[front:(len(data) - end)]
    
    return new_data

data = [5, 4, 8, 1, 4, 6, 2, 7]
front = int(input("Enter amount of variables to take from front of the array: "))
end = int(input("Enter amount of variables to take from the end of the array: "))

new_data = delete_data_range(data, front, end)
print(data)
print(new_data)



