#If you have a string has “i” character in it, print the location of the character.

str_input = input("Enter a string: ")
index = 0

for char in str_input:
    if char == 'i':
        print(f"Found 'i' at index: {index}")
    index += 1