import os
import sys
import json
from utils.validators import validate_email, validate_password
from models.user import User

db_path = "data/db.json"
    
def get_users():
    if os.path.isfile(db_path):
        try:
            with open(db_path, mode="rt", encoding="utf-8") as f:
                return json.load(f)
        except:
            sys.stderr.write("Error: fetch data")
    else:
        sys.stderr.write("Error: db connection")

def create_user(name: str, email: str, password: str, role: str) -> bool:
    data = get_users()
    if data["users"] is None:
        return False
    if validate_email(data["users"], len(data["users"]) + 1, email)  == False or validate_password(name, password) == False:
        return False
    user = User(len(data["users"]) + 1, name, email, password, role)
    data["users"].append(user.to_dict())
    obj = json.dumps(data, indent=4)
    with open(db_path, mode="wt", encoding="utf-8") as f:
        f.write(obj)
    return True

def update_user(id: int, name: str, email: str, password: str, role: str) -> bool:
    data = get_users()
    if data["users"] is None:
        return False
    if validate_email(data["users"], id, email) == False or validate_password(name, password) == False:
       return False
    filter = [user for user in data["users"] if user["id"] == id]
    if len(filter) == 1:
        user = User(id, name, email, password, role)
        filter[0].update(user.to_dict())
    else:
        sys.stderr.write("Error: user not found")
        return False
    obj = json.dumps(data, indent=4)
    with open(db_path, mode="wt", encoding="utf-8") as f:
        f.write(obj)
    return True
    
def patch_user(id: int, **kwargs) -> bool:
    data = get_users()
    if data["users"] is None:
        return False
    if len(kwargs) != 1:
        sys.stderr.write("Error: invalid body content")
        return False
    exist = [k for k in kwargs if k in 'idnameemailpasswordrole']
    if len(exist) == 0:
        sys.stderr.write("Error: invalid field")
        return False
    filter = [user for user in data["users"] if user["id"] == id]
    if len(filter) == 1:
        for key in kwargs.keys():
            if key == 'email':
                if validate_email(data["users"], (filter[0])['id'], kwargs[key]) == False:
                    return False
            elif key == 'password':
                if validate_password((filter[0])['name'], kwargs[key]) == False:
                    return False
        filter[0].update(kwargs)
    else:
        sys.stderr.write("Error: user not found")
        return False
    obj = json.dumps(data, indent=4)
    with open(db_path, mode="wt", encoding="utf-8") as f:
        f.write(obj)
        return True

def delete_user(id: int) -> bool:
    data = get_users()
    if data["users"] is None:
        return False
    count = 0
    for user in data["users"]:
        if user["id"] == id:
            data["users"].pop(count)
            obj = json.dumps(data, indent=4)
            with open(db_path, mode="wt", encoding="utf-8") as f:
                f.write(obj)
                return True
        count += 1
    sys.stderr.write("Error: Not found\n")
    return False
