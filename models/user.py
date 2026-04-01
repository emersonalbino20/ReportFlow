import os
import sys
import json
from utils.validators import validate_email, validate_password

class User:
    
    def __init__(self):
        self.db_path = "data/db.json"
    
    def get(self):
        if os.path.isfile(self.db_path):
            try:
                with open(self.db_path, mode="rt", encoding="utf-8") as f:
                    return json.load(f)
            except:
                sys.stderr.write("Error: fetch data")
        else:
            sys.stderr.write("Error: db connection")

    def post(self, name: str, email: str, password: str, role="teacher") -> None:
        data = self.get()
        if data is None:
            return
        if validate_email(data, len(data) + 1, email)  == False or validate_password(name, password) == False:
           return None
        data.append({ "id": len(data) + 1, "name": name, "email": email, "password": password, "role": role})
        obj = json.dumps(data, indent=4)
        with open(self.db_path, mode="wt", encoding="utf-8") as f:
            f.write(obj)

    def put(self, id: int, name: str, email: str, password: str, role: str) -> None:
        data = self.get()
        if data is None:
            return
        if validate_email(data, id, email) == False or validate_password(name, password) == False:
           return None
        filter = [user for user in data if user["id"] == id]
        if len(filter) == 1:
            filter[0].update({ "id": id, "name": name, "email": email, "password": password, "role": role})
        else:
            return sys.stderr.write("Error: user not found")
        obj = json.dumps(data, indent=4)
        with open(self.db_path, mode="wt", encoding="utf-8") as f:
            f.write(obj)
    
    def patch(self, id, **kwargs):
        data = self.get()
        if data is None:
            return 
        if len(kwargs) != 1:
            return sys.stderr.write("Error: invalid body content")
        exist = [k for k in kwargs if k in 'idnameemailpasswordrole']
        if len(exist) == 0:
            return sys.stderr.write("Error: invalid field")
        filter = [user for user in data if user["id"] == id]
        if len(filter) == 1:
            for key in kwargs.keys():
                if key == 'email':
                    if validate_email(data, (filter[0])['id'], kwargs[key]) == False:
                        return
                elif key == 'password':
                    if validate_password((filter[0])['name'], kwargs[key]) == False:
                        return
            filter[0].update(kwargs)
        else:
            return sys.stderr.write("Error: user not found")
        obj = json.dumps(data, indent=4)
        with open(self.db_path, mode="wt", encoding="utf-8") as f:
            f.write(obj)

    def delete(self, id: int):
        data = self.get()
        if data is None:
            return
        count = 0
        for user in data:
            if user["id"] == id:
                data.pop(count)
                obj = json.dumps(data, indent=4)
                with open(self.db_path, mode="wt", encoding="utf-8") as f:
                    f.write(obj)
                break
            count += 1
       

prof = User()
prof.patch(2, email="francis@fmail")
# prof.put(0, "hole da silva", "hole@fmail", "1221", "cordinator")
# prof.delete(20)