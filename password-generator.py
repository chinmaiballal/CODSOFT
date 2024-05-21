import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    # Get desired password length from user
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for the length.")

    # Generate and print password
    password = generate_password(length)
    print("Generated Password:", password)

