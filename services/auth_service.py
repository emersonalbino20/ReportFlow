import sys
from services.user_service import create_user, get_user

def register_user():
    if create_user(input("Name: "), input("Email: "), input("Password: "), input("Role: ")):
        print("Registered!")
    else:
        sys.stderr.write("Failed!\n")

def login():
    name = input("Name: ")
    passw = input("Passoword: ")
    data = get_user()
    if len(data) == 0:
        return sys.stderr.write("No register\n")
    user = [user for user in data if user["name"] == name and user["password"] == passw]
    if len(user) == 1:
        print("Wellcome Mr. {} {}".format(user[0]["role"], user[0]["name"]))
    else:
        sys.stderr.write("Not registerd!\n")

login()
