# Q4. Write a program that implements a simple JSON-like data validator, checking that a dictionary
# matches a given schema (required keys and types).

def validate_schema(data, schema):
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"Missing key: {key}")
        elif not isinstance(data[key], expected_type):
            errors.append(f"Wrong type for {key}: expected {expected_type.__name__}")
    return errors
schema = {"name": str, "age": int, "active": bool}
data = {"name": "Aarav", "age": "22", "active": True}
errors = validate_schema(data, schema)
print(errors if errors else "Valid data")