while True:
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty! Try again.")
    elif name.isdigit():
        print("Name cannot be just numbers! Try again.")
    else:
        print(f"Welcome, {name}!")
        break

while True:
    email = input("Enter your email: ").strip()

    if "@" in email:
        print("Valid Email!")
        break
    else:
        print("False\nPlease enter a valid email.")

print("User Profile:\nName: " + name + "\nEmail: " + email)
        