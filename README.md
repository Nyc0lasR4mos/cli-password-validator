# CLI Password Validator

CLI application written in Python for validating passwords using configurable security rules, modular architecture, and clear separation of responsibilities.

|        Rule       | Default Value | Description                                  |
| :---------------: | :------------ | :------------------------------------------- |
|   Minimum Length  | 8 characters  | Password must contain at least 8 characters. |
|  Uppercase Letter | Required      | At least one uppercase letter (A-Z).         |
|  Lowercase Letter | Required      | At least one lowercase letter (a-z).         |
|       Number      | Required      | At least one numeric digit (0-9).            |
| Special Character | Required      | At least one special character (!@#$%^&*()). |

The validation rules are loaded from the `config/rules.json` file, allowing the application's behavior to be customized without modifying the source code.

The validator checks every configured requirement and returns all unmet criteria at once, providing clear and actionable feedback instead of stopping at the first validation error.

## Prerequisites

Required Python version: **Python 3.8 or higher**.

pip installed.

## Installation

Clone the repository:

```bash
git clone https://github.com/SEU_USUARIO/cli-password-validator.git
cd cli-password-validator
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The validation rules are stored in:

```text
config/rules.json
```

Example configuration:

```json
{
    "min_length": 12,
    "require_special": true
}
```

The following properties can be customized:

|      Property     |   Type  | Default | Description                              |
| :---------------: | :-----: | :-----: | :--------------------------------------- |
|     min_length    | Integer |    8    | Minimum password length.                 |
| require_uppercase | Boolean |   true  | Requires at least one uppercase letter.  |
| require_lowercase | Boolean |   true  | Requires at least one lowercase letter.  |
|   require_number  | Boolean |   true  | Requires at least one numeric digit.     |
|  require_special  | Boolean |   true  | Requires at least one special character. |

## How to Run

Execute the application from the project's root directory:

```bash
python main.py
```

**The application runs in the terminal, so the expected prompt will be:**

Input: **Enter your password**

The user enters either a valid or an invalid password.

For a valid password, the application returns:

```text
Password is valid!
```

For an invalid password, the application returns every unmet validation rule.

## Running Tests

```bash
python -m pytest tests/test_validator.py -v
```

For unit testing.

---

## Below are some examples of *successful and failed* validations

> [!TIP]
> **Success**
>
> **Input:**
>
> MySecureP@ss123
>
> **Output:**
>
> Password is valid!

> [!CAUTION]
> **Validation Error**
>
> **Input:**
>
> password
>
> **Output:**
>
> Invalid password:
>
> * Your password must contain at least one uppercase letter.
> * Your password must contain at least one number.
> * Your password must contain at least one special character (!@#$%^&*()).

## Technical Decisions

The application follows the Separation of Concerns principle. The `validator.py` module contains only the password validation logic, making it independent of user input and file handling. The `config_loader.py` module is responsible for loading the JSON configuration and gracefully falls back to secure default rules if the configuration file is missing or invalid. Finally, the `cli.py` module manages all terminal interaction, keeping the business logic isolated and easily reusable in other environments, such as web APIs.

**Nycolas Ramos**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge\&logo=linkedin\&logoColor=0A66C2)](https://www.linkedin.com/in/nycolas-ramos-483810399/) [![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge\&logo=github\&logoColor=FFFFFF)](https://github.com/Nyc0lasR4mos)
