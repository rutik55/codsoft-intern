import random
import string
def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lower_case + upper_case + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
            else:
                password = generate_password(length)
                print("Generated Password:", password)
                print("="*50)
                a=input(" Do you want to generate one more password (YES/NO):")
                if(a=="NO"):
                    print("Thanks for using our PASSWORD GENERATOR")
                    break
        except ValueError:
             print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
