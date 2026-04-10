import sys
import time
from db.init import init_db
from utils.connect import simulate
from services.auth_service import login, register_user
from services.user_service import get_users
from visualizations import list_users
from menus.main_menu import main_menu
from menus.user_menu import user_menu
from menus.report_menu import report_menu

def clean():
    print("\033c")
    print("Invalid option")
    time.sleep(1)

if sys.platform != 'linux':
    sys.stderr.write("Error: run on linux plataform\n")
    quit()
else:
    simulate()
    init_db()
    attempt = 0
    while True:
        print("\033c")
        main_menu()
        option = input(": ")
        if option.isnumeric() == False:
            clean()
            continue
        if option == "1":
            print("\033c")
            current_user = login()
            while current_user == None:
                attempt += 1
                print("\033c")
                if attempt == 3:
                    attempt = 0
                    break
                print("Attempts: ", attempt)
                current_user = login()
            else:
                print("\033c")
                while True:
                    print("\033c")
                    user_menu(current_user["role"])
                    user_option = input(": ")
                    if user_option.isnumeric() == False:
                        clean()
                        continue
                    elif (user_option == "1"
                            and current_user["role"] == "coordinator"):
                        print("\033c")
                        register_user()
                        time.sleep(2)
                    elif (user_option == "2"
                            and current_user["role"] == "coordinator"):
                        print("\033c")
                        list_users(get_users())
                        time.sleep(2)
                    elif (user_option == "3" 
                            and current_user["role"] == "coordinator"):
                        print("\033c")
                        while True:
                            print("\033c")
                            report_menu(current_user["role"])
                            report_option = input(": ")
                            if report_option.isnumeric() == False:
                                print("Invalid option")
                                time.sleep(1)
                                continue
                            elif report_option == "1":
                                print("\033c")
                                print("All teacher reports")
                            elif report_option == "2":
                                print("\033c")
                                print("All date reports")
                            elif report_option == "3":
                                print("\033c")
                                break
                            else:
                                print("\033c")
                                print("Invalid option")
                                time.sleep(1)
                    elif (user_option == "1"
                            and current_user["role"] == "teacher"):
                        print("\033c")
                        print("Registering report")
                    elif (user_option == "2"
                            and current_user["role"] == "teacher"):
                        print("\033c")
                        print("My reports...")
                    elif user_option == "0":
                        print("\033c")
                        break
                    else:
                       clean()
        elif option == "0":
            break
        else:
           clean()
