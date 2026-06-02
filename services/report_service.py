import os
import sys
import json
from utils.utils import catch_error
from services.user_service import get_user_by_id
from models.report import Report

db_path = "data/db.json"

def get_reports():
    if os.path.isfile(db_path):
        try:
            with open(db_path, mode="rt", encoding="utf-8") as f:
                return json.load(f)
        except:
            sys.stderr.write("Error: fetch data\n")
    else:
        sys.stderr.write("Error: db connection\n")

@catch_error
def get_teacher_reports(user_id: int) -> list | None:
    data = get_reports()
    if data["reports"] is None:
        return None
    return [report for report in data["reports"] if report["user_id"] == user_id]

@catch_error
def get_report_by_date(date: str) -> list | None:
    data = get_reports()
    if data["reports"] is None:
        return None
    return [report for report in data["reports"] if report["date"] == date]

@catch_error
def create_report(
        user_id: int, date: str, 
        content: str) -> bool:
    data = get_reports()
    user = get_user_by_id(user_id)
    if data["reports"] is None or user is None:
        return False
    if (Report.validate_date(date) == False 
            or Report.validate_content(content) == False):
        return False
    report = Report(len(data["reports"]) + 1, user_id, date, content)
    data["reports"].append(report.to_dict)
    obj = json.dumps(data, indent=4)
    with open(db_path, mode="wt", encoding="utf-8") as f:
        f.write(obj)
    return True

@catch_error
def update_report(
        id: int, user_id :int, date: str,
        content: str) -> None:
    data = get_reports()
    user = get_user_by_id(user_id)
    if data["reports"] is None or user is None:
        return False
    if (Report.validate_date(date) == False 
            or Report.validate_content(content) == False):
        return False
    filter = [report for report in data["reports"] if report["id"] == id]
    if len(filter) == 1:
        report = Report(id, user_id, date, content)
        filter[0].update(report.to_dict)
    else:
        sys.stderr.write("Error: report not found\n")
        return False
    obj = json.dumps(data, indent=4)
    with open(db_path, mode="wt", encoding="utf-8") as f:
        f.write(obj)
    return True

@catch_error
def patch_report(id: int, **kwargs) -> bool:
    data = get_reports()
    if data["reports"] is None:
        return False
    if len(kwargs) != 1:
        sys.stderr.write("Error: invalid body content")
        return False
    exist = [k for k in kwargs if k in 'iddatecontent']
    if len(exist) == 0:
        sys.stderr.write("Error: invalid field")
        return False
    filter = [report for report in data["reports"] if report["id"] == id]
    if len(filter) == 1:
        for key in kwargs.keys():
            if key == 'date':
                if Report.validate_date(kwargs[key]) == False:
                    return False
            elif key == 'content':
                if Report.validate_content(kwargs[key]) == False:
                    return False
        filter[0].update(kwargs)
    else:
        sys.stderr.write("Error: report not found\n")
        return False
    obj = json.dumps(data, indent=4)
    with open(db_path, mode="wt", encoding="utf-8") as f:
        f.write(obj)
    return True

@catch_error
def delete_report(id: int) -> bool:
    data = get_reports()
    if data["reports"] is None:
        return False
    count = 0
    for report in data["reports"]:
        if report["id"] == id:
            data["reports"].pop(count)
            obj = json.dumps(data, indent=4)
            with open(db_path, mode="wt", encoding="utf-8") as f:
                f.write(obj)
            return True
        count += 1
    sys.stderr.write("Error: report not found\n")
    return False
