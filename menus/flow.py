from services.auth_service import login, register_user, register_report
from services.user_service import get_users
from services.report_service import get_reports, get_teacher_reports, get_report_by_date
from views import list_users, list_reports, list_teacher_reports, list_date_reports
from menus.user_menu import user_menu
from menus.report_menu import report_menu
from models.report import Report
from utils.clean import clean, clear_screen
from time import sleep

def login_with_attempts():
    attempt = 0
    while attempt < 3:
        clear_screen()
        user = login()
        if user:
            return user
        attempt += 1
        if attempt > 0 : print(f"Missing {3 - attempt} attempts") 
        sleep(2)
    return None

def route_user(user):
    if user["role"] == "coordinator":
        coordinator_flow(user)
    elif user["role"] == "teacher":
        teacher_flow(user)

def teacher_flow(user):
    while True:
        clear_screen()
        print("****Welcome {0:s} {1:s}!****".format(user["role"], user["name"]))
        user_menu(user["role"])
        option = input(": ")
        if option == "1":
            clear_screen()
            register_report(user["id"])
            sleep(2)
        elif option == "2":
            clear_screen()
            list_teacher_reports(get_teacher_reports(user["id"]))
            back_menu()
        elif option == "0":
            break
        else:
            clean()

def coordinator_flow(user):
    while True:
        clear_screen()
        print("****Welcome {0:s} {1:s}!****".format(user["role"], user["name"]))
        user_menu(user["role"])
        option = input(": ")
        if option == "1":
            clear_screen()
            register_user()
            sleep(2)
        elif option == "2":
            clear_screen()
            list_users(get_users())
            back_menu()
        elif option == "3":
            report_flow(user)
        elif option == "0":
            break
        else:
            clean()

def report_flow(user):
    while True:
        clear_screen()
        report_menu(user["role"])
        option = input(": ")
        if option == "1":
            clear_screen()
            print("Insert teacher id: ")
            input_id = input(": ")
            if not input_id.isnumeric():
                clean()
                continue
            list_teacher_reports(get_teacher_reports(int(input_id)))
            back_menu()
        elif option == "2":
            clear_screen()
            print("Insert date (yyyy-mm-dd): ")
            input_date = input(": ")
            if Report.validate_date(input_date) == False:
                clear_screen()
                print("Invalid date format")
                sleep(2)
                continue
            list_date_reports(get_report_by_date(input_date))
            back_menu()
        elif option == "3":
            clear_screen()
            list_reports(get_reports())
            back_menu()
        elif option == "4":
            break
        else:
            clean()

def back_menu():
    while True:
        option = input("1 - Back: ")
        if option == "1":
            break