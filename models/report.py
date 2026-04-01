class Report:
    def __init__(self, id: int, user_id: int, date: str, content: str):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "date": self.date,
            "content": self.content
        }
