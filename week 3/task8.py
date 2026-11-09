#Start with an empty list called numbers. Use a loop to append numbers 1 to 5 into the list, then print the final list.
numbers = []
for i in range(1, 6):
    numbers.append(i)
    print(f"Current list: {numbers}")
print(f"Final list: {numbers}")