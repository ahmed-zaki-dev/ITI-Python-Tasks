#Convert a list of names into sorted dictionary which key is the Alpha.
#and value is a list of names corresponding to this alpha.

list_names = ["Ahmed", "Ali", "Mohamed", "Tarek", "Zeyad"]
list_names.sort()

dict_names = {}

for name in list_names:
    first_char = name[0]
    
    if dict_names.get(first_char) == None:
        dict_names[first_char] = []
    
    dict_names[first_char].append(name)

print(dict_names)