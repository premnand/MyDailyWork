import random
import string

def generate_password(length):
    # Define the character set: lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly choosing characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
