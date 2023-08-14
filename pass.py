import random
import string

def generate_password(length, c):
    characters = ""
    if c == "Easy":
        characters = string.ascii_letters
    elif c == "Medium":
        characters = string.ascii_letters + string.digits
    elif c == "Hard":
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = []
    
    for _ in range(length):
        password.append(random.choice(characters))
    
    return ''.join(password)

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a valid password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    complexity_levels = ["Easy", "Medium", "Hard"]
    print("Choose complexity level:")
    for index, level in enumerate(complexity_levels, start=1):
        print(f"{index}. {level}")
    
    while True:
        try:
            complexity_choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= complexity_choice <= len(complexity_levels):
                complexity = complexity_levels[complexity_choice - 1]
                break
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    generated_password = generate_password(length, complexity)
    print("Generated Password:", generated_password)

if __name__ == "__main__":
    main()
