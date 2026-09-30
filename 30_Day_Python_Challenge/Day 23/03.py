# Q3. Write a program to use regular expressions to validate whether a given string is a valid email
# address.

import re
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))