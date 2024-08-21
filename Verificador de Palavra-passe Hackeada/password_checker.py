# About password security levels
# Many organizations require complex passwords as part of their security policies. Certain regulations, such as the General Data Protection Regulation (GDPR), require organizations to take steps to ensure the security of personal data, which includes using complex passwords.

# Zendesk strongly suggests setting the Recommended password security level for both team members and end users to safeguard your account.

# When the Recommended password security level is set, passwords must meet the following requirements:
# Must be at least 12 characters
# Five attempts allowed before a temporary 10-minute lockout
# Must include uppercase and lowercase letters (a-z and A-Z)
# Must include a number (0-9)
# Must include a special character (!, @, #, %, etc.)
# Must not include the word "Zendesk"
# Must not resemble an email address
# Must pass a check against a list of known breached passwords

import json
import os

# Constants
JSON_FILE = 'pwned_passwords.json'

def load_pwned_passwords():
    """Load pwned passwords from JSON file."""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, 'r') as file:
                # Ensure that we are loading a list of strings
                pwned_passwords = json.load(file)
                if isinstance(pwned_passwords, list):
                    print(f"Loaded pwned passwords: {pwned_passwords}")  # Debugging line
                    return pwned_passwords
                else:
                    print("Error: The JSON file does not contain a list.")
                    return []
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
            return []
    else:
        print(f"Error: JSON file '{JSON_FILE}' does not exist.")
        return []

def check_password(password):
    """Check if the given password is pwned."""
    pwned_passwords = load_pwned_passwords()
    print(f"Checking password: {password}")  # Debugging line
    print(f"Loaded pwned passwords for checking: {pwned_passwords}")  # Debugging line
    if isinstance(pwned_passwords, list) and password in pwned_passwords:
        print(f"Password '{password}' is pwned.")  # Debugging line
        return True
    else:
        print(f"Password '{password}' is not pwned.")  # Debugging line
        return False

if __name__ == '__main__':
    user_password = input("Introduza sua palavra-passe: ")
    print(f"User entered password: {user_password}")  # Debugging line
    if check_password(user_password):
        print("Sua palavra-passe foi comprometida!")
    else:
        print("Sua palavra-passe não está na base de dados de senhas comprometidas.")
    
    
    

