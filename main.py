import sys
from db.init import init_db
from utils.connect import simulate
from menus.main_menu import main_menu
from menus.flow import clear_screen, login_with_attempts, route_user
from utils.clean import clean

if sys.platform != 'linux':
    sys.stderr.write("Error: run on linux plataform\n")
    quit()
else:
    simulate()
    init_db()
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
