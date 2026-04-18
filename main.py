import sys
import time
from db.init import init_db
from utils.connect import simulate
from services.auth_service import login, register_user, register_report
from services.user_service import get_users
from services.report_service import get_reports
from visualizations import list_users, list_reports
from menus.main_menu import main_menu
from menus.user_menu import user_menu
from menus.report_menu import report_menu

def clean():
    print("\033c")
    print("Invalid option")
    time.sleep(1)

def clear_screen():
    print("\033c")

def login_with_attempts():
    attempt = 0
    while attempt < 3:
        clear_screen()
        user = login()
        if user:
            return user
        attempt += 1
        print(f"Attempts: {attempt}")
    return None

def route_user(user):
    if user["role"] == "coordinator":
        coordinator_flow(user)
    elif user["role"] == "teacher":
        teacher_flow(user)

def teacher_flow(user):
    while True:
        clear_screen()
        teacher_menu(user["role"])
        option = input(": ")
        if option == "1":
            register_report(user["id"])
            time.sleep(2)
        elif option == "2":
            print("My reports...")
        elif option == "0":
            break
        else:
            clean()

def coordinator_flow(user):
    while True:
        clear_screen()
        user_menu(user["role"])
        option = input(": ")
        if option == "1":
            register_user()
            time.sleep(2)
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
            print("All teacher reports")
        elif option == "2":
            print("All date reports")
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

if sys.platform != 'linux':
    sys.stderr.write("Error: run on linux plataform\n")
    quit()
else:
    simulate()
    init_db()
    attempt = 0
    def main():
        while True:
            clear_screen()
            main_menu()
            option = input(": ")
            if not option.isnumeric():
                clean()
                continue
            if option == "1":
                user = login_with_attempts()
                if user:
                    route_user(user)
            elif option == "0":
                break
            else:
                clean()
    main()
