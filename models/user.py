import os
import sys
import json
from utils.validators import validate_email

class User:
    def __init__(self):
        pass
    
    def get(self):
        if os.path.isfile("data/db.json"):
            try:
                with open("data/db.json", mode="rt", encoding="utf-8") as f:
                    return json.load(f)
            except:
                sys.stderr.write("Error: fetch data")
        else:
            sys.stderr.write("Error: db connection")

    def post(self, name: str, email: str, password: str, id=0, role="teacher") -> None:
        data = self.get()
        if data is None:
            return
        if validate_email(email) == False:
           return sys.stderr.write("Error: invalid email")
        data.append({ "id": id, "name": name, "email": email, "password": password, "role": role})
        obj = json.dumps(data, indent=4)
        with open("data/db.json", mode="wt", encoding="utf-8") as f:
            f.write(obj)

    def put(self, id: int, name: str, email: str, password: str, role: str) -> None:
        data = self.get()
        if data is None:
            return
        if validate_email(email) == False:
           return sys.stderr.write("Error: invalid email")
        filter = [user for user in data if user["id"] == id]
        if len(filter) == 1:
            filter[0].update({ "id": id, "name": name, "email": email, "password": password, "role": role})
        else:
            return
        obj = json.dumps(data, indent=4)
        with open("data/db.json", mode="wt", encoding="utf-8") as f:
            f.write(obj)

prof = User()
# prof.post("emerson", "email@gmail", "a", 1, "teacher")
# prof.put(0, "hole da silva", "hole@fmail", "1221", "cordinator")
print(prof.get())