#Write a program that accepts a hyphen-separated input and print the words in a colon-separated sequence after sorted it alphabetically​

string = input("Enter a hyphen-separated string: ")
words = string.split("-")
for i in range(len(words)):
    words[i] = words[i].strip()
    words[i] = words[i].lower()
    
words.sort()
print("The sorted words are: ", ":".join(words))