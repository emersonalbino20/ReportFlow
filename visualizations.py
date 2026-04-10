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