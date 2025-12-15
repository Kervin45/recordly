class Record:
    def __init__(self, id, title, content, tags, created_at, updated_at):
        self.id = id
        self.title = title
        self.content = content
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_row(cls, row):
        return cls(*row)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

