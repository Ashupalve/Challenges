# Q4. Write a program to use regular expressions to extract all phone numbers from a block of text.

import re
text = "Call me at 987-654-3210 or 123-456-7890 for details."
pattern = r"\d{3}-\d{3}-\d{4}"
numbers = re.findall(pattern, text)
print(numbers)