def list_users(users: dict):
    data = users
    print("{0:<5}{1:10}{2:<10}\n".format("ID", "NAME", "EMAIL"))
    for user in data["users"]:
        for key, value in user.items():
            if key == "id":
                print("{0:<5}".format(value), end="")
            elif key == "name":
                print("{0:10}".format(value), end="")
            elif key == "email":
                print("{0:<10}".format(value), end=" ")
        print()

def list_reports(reports: dict):
    data = reports
    print("{0:<5}{1:<5}{2:>10}{3:>10}\n".format("ID", "TEACHER", "DATE", "CONTENT"))
    for reports in data["reports"]:
        for key, value in reports.items():
            if key == "id":
                print("{0:<5}".format(value), end="")
            if key == "user_id":
                print("{0:<5}".format(value), end="")
            elif key == "date":
                print("{0:>10}".format(value), end="")
            elif key == "content":
                print("{0:10}".format(value), end=" ")
        print()