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

# Constantes
json_file = 'pwned_passwords.json'

def load_pwned_passwords():
    # Carrega senhas comprometidas a partir do arquivo JSON.
    if not os.path.exists(json_file):
        print(f"Erro: O arquivo JSON '{json_file}' não existe.")
        return []
    try:
        with open(json_file, 'r') as file:
            pwned_passwords = json.load(file)
            if isinstance(pwned_passwords, list):
                return pwned_passwords
            else:
                print("Erro: O arquivo JSON não contém uma lista.")
                return []
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formatado.")
        return []

def check_password(password):
    """Verifica se a senha fornecida está comprometida."""
    pwned_passwords = load_pwned_passwords()
    return password in pwned_passwords

if __name__ == '__main__':
    user_password = input("Introduza sua palavra-passe: ")
    if check_password(user_password):
        print("Sua palavra-passe foi comprometida!")
    else:
        print("Sua palavra-passe não está na base de dados de senhas comprometidas.")

    
    
    

