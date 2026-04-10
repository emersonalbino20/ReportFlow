def report_menu(role: str):
    if role == "teacher":
        print("1 - Register report")
        print("2 - My reports")
        print("0 - Logout")
    elif role == "coordinator":
        print("1 - Reports by teacher")
        print("2 - Reports by date")
        print("3 - Back")
    else:
        quit()