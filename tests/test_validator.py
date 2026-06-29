import pytest
from src.validator import validate_password

DEFAULT_RULES = {
    "min_length": 8,
    "require_uppercase": True,
    "require_lowercase": True,
    "require_number": True,
    "require_special": True
}

test_cases = [
    # Test passwords that meet all criteria
    ("ValidPassword123!", True),

    # Test each criterion individually
    ("password", False),          # Missing uppercase, number, and special character
    ("PASSWORD", False),          # Missing lowercase, number, and special character
    ("Password123", False),       # Missing special character
    ("Password!", False),         # Missing number
    ("12345678", False),          # Missing letters and special character

    # Test with custom rules

    # Minimum length
    ("ValidPassword123!", True, {"min_length": 12}),
    ("ValidPassword123!", True, {"min_length": 16}),

    # Uppercase requirement
    ("validpassword123!", False, {"require_uppercase": True}),
    ("validpassword123!", True, {"require_uppercase": False}),

    # Lowercase requirement
    ("VALIDPASSWORD123!", False, {"require_lowercase": True}),
    ("VALIDPASSWORD123!", True, {"require_lowercase": False}),

    # Number requirement
    ("ValidPassword!", False, {"require_number": True}),
    ("ValidPassword!", True, {"require_number": False}),

    # Special character requirement
    ("ValidPassword123", False, {"require_special": True}),
    ("ValidPassword123", True, {"require_special": False}),
]

@pytest.mark.parametrize("password, expected_valid, custom_rules", test_cases)
def test_password_validation(password, expected_valid, custom_rules):
    # 1. Merges standard rules with custom test rules
    rules = {**DEFAULT_RULES, **custom_rules}
    
    # 2. Call the validate_password function with the test password and rules
    errors = validate_password(password, rules)
    
    # 3. Verify if the password is valid based on the presence of errors
    is_valid = len(errors) == 0
    
    assert is_valid == expected_valid, f"Senha '{password}' falhou. Erros: {errors}"