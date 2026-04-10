from menus.report_menu import report_menu

def user_menu(role: str):
    if role == "coordinator":
        print("1 - Register User")
        print("2 - List Teacher")
        print("3 - Reports")
        print("0 - logout")
    elif role == "teacher":
        report_menu(role)
    else:
        quit()