import sys
from services.user_service import create_user, get_users
from services.report_service import create_report

def register_user():
    name = input("Name: ")
    email = input("Email: ")
    passw = input("Password: ")
    role = input("Role: ")
    if create_user(name, email, passw, role):
        print("Registered!")
    else:
        sys.stderr.write("Failed!\n")

def register_report(user_id: int):
    date = input("Date: ")
    content = input("Content: ")
    if create_report(user_id, date, content):
        print("Registered!")
    else:
        sys.stderr.write("Failed!\n")

def login():
    data = get_users()
    if len(data) == 0:
        return sys.stderr.write("No register\n")
    name = input("Name: ")
    passw = input("Password: ")
    user = [user for user in data["users"] if user["name"] == name and user["password"] == passw]
    if len(user) == 1:
        return user[0]
    else:
        return None
