def validate_password(password, rules=None):
    """Validate the password and return a list of error messages."""
    if rules is None:
        rules = {}

    errors = []  # List to store error messages.
    min_length = rules.get("min_length", 8)  # Configurable, default: 8 characters
    require_uppercase = rules.get("require_uppercase", True)
    require_lowercase = rules.get("require_lowercase", True)
    require_number = rules.get("require_number", True)
    require_special = rules.get("require_special", True)

    if len(password) < min_length:
        errors.append(f"Your password must be at least {min_length} characters long.")
    if require_uppercase and not any(char.isupper() for char in password):
        errors.append("Your password must contain at least one uppercase letter.")
    if require_lowercase and not any(char.islower() for char in password):
        errors.append("Your password must contain at least one lowercase letter.")
    if require_number and not any(char.isdigit() for char in password):
        errors.append("Your password must contain at least one number.")
    if require_special and not any(char in "!@#$%^&*()" for char in password):
        errors.append("Your password must contain at least one special character (!@#$%^&*()).")

    return errors  # Return the list of error messages. If empty, the password is valid.

