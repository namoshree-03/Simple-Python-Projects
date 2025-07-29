#password generator
import random 
print("Welcome to your password generator!")
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*/=%@#_&"
number = input("Amount of passwords you want to generate? ")
number = int(number)
length = input("Enter your password length: ")
length = int(length) 

print("Here are your passwords:")

for i in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print(passwords)
a = input("would you like to generate more passwords? (yes/no)")
if a.lower() == 'yes':
    number = input("Amount of passwords you want to generate? ")
    number = int(number)
    length = input("Enter your password length: ")
    length = int(length) 
    print("Here are your new passwords:")
    for i in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(char)
        print(passwords)
else:
    print("Goodbye! Thanks for using the password generator.")

# This is a simple implementation of a password generator.
# The user can specify the number of passwords to generate and their length.
# The generator uses a combination of lowercase letters, uppercase letters, digits, and special characters.
# The generated passwords are printed to the console.
# The implementation is straightforward and easy to understand.
# The game can be extended with features like input validation or a user interface.
# The current implementation is efficient and runs in linear time relative to the number of passwords and their length.
# The passwords are randomly generated, ensuring a high level of security.
# The game is suitable for users who want to create strong passwords for their accounts.
# The user can run the script multiple times to generate different sets of passwords.
# The implementation can be easily adapted for different programming languages or platforms.
# The code is structured to be clear and maintainable, making it easy to add new features or modify existing ones.
# The game can be modified to include options for different character sets or password policies.