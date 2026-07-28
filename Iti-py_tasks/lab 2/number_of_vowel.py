#You have a string, count the number of vowels in this string.

str_input = input("Enter a string: ").lower()
count = 0

for char in str_input:
    if char in "aeiou":
        count += 1

print(f"number of vowels in ur string is: {count}")