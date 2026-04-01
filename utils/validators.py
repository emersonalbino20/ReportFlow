import re
import sys

def validate_email(data: dict, id: int, email: str) -> bool:
    if data:
        filter = [user for user in data if user["email"] == email]
        if filter and filter[0]['id'] != id:
            sys.stderr.write("Error: email already exist\n")
            return False
    if re.match(r"[\w\.-]+@[\w\.-]+", email):
        return True
    else:
        sys.stderr.write("Error: invalid email\n")
        return False

def validate_password(name: str, password: str) -> bool:
    if (len(password) != 8):
        sys.stderr.write("Error: password length should be 8\n")
        return False
    elif (name in password):
        sys.stderr.write("Error: password should not contains username\n")
        return False
    elif (password.islower() or password.isupper()):
        sys.stderr.write("Error: password should have at least an upper and a lower letter\n")
        return False
    elif (password.isalpha() or password.isalpha()):
        sys.stderr.write("Error: password should contain letters and number\n")
        return False
    else:
        return True
