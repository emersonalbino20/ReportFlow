import sys
from db.init import init_db
from utils.connect import simulate

if sys.platform != 'linux':
    sys.stderr.write("Error: run on linux plataform\n")
    quit()
else:
    simulate()
    init_db()
    print("\033c")

