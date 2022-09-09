import sys
import re

class Report:
    def __init__(
            self, id: int, user_id: int,
            date: str, content: str):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.content = content

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "date": self.date,
            "content": self.content
        }

    @staticmethod
    def validate_date(date: str):
        if len(date) == 10 and re.search(r"\d\d\d\d-\d\d-\d\d", date):
            return True
        sys.stderr.write("Error: invalid date\n")
        return False
    
    @staticmethod
    def validate_content(content: str) -> bool:
        if len(content) < 10:
            sys.stderr.write("Error: content should have more than 9 chars\n")
            return False
        return True
