import re

def validate_email(email: str) -> bool:
    if re.match(r"[\w\.-]+@[\w\.-]+", email):
        return True
    else:
        return False