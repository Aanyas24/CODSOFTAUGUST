import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_special_chars=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Please enable at least one character type.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        generated_password = generate_password(password_length, use_letters, use_digits, use_special_chars)
        
        if generated_password:
            print("Generated Password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
