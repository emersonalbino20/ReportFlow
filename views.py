from tabulate import tabulate
from utils.utils import to_list

def list_users(users: dict):
    table = to_list(users["users"], True)
    headers = ["ID", "NAME", "EMAIL", "ROLE"]
    print(tabulate(table, headers, tablefmt="grid"))

def list_reports(reports: dict):
    table = to_list(reports["reports"], False)
    headers = ["ID", "TEACHER ID", "DATE", "CONTENT"]
    print(tabulate(table, headers, tablefmt="grid"))

def list_teacher_reports(reports: dict):
    table = to_list(reports, False)
    headers = ["ID", "TEACHER ID", "DATE", "CONTENT"]
    print(tabulate(table, headers, tablefmt="grid"))

def list_date_reports(reports: dict):
    table = to_list(reports, False)
    headers = ["ID", "TEACHER ID", "DATE", "CONTENT"]
    print(tabulate(table, headers, tablefmt="grid"))