from src.validator import validate_password
from src.config_loader import load_config

def main():
    config = load_config("config/rules.json")
    password = input("Enter a password to validate: ")
    errors = validate_password(password, config)
    
    if not errors:
        print("\033[92mPassword is valid!\033[0m")  # Green text
    else:
        print("\033[91mInvalid password:\033[0m")  # Red text
        for error in errors:
            print(f" - {error}")