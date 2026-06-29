def load_config(file_path):
    import json
    default_rules = {
        "min_length": 8,
        "require_uppercase": True,
        "require_lowercase": True,
        "require_number": True,
        "require_special": True
    }

    try:
        with open(file_path, "r") as f:
            config = json.load(f)
        return {**default_rules, **config}
    except (FileNotFoundError, json.JSONDecodeError):
        return default_rules

