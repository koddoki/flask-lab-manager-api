from mongoengine import Document, StringField, IntField, ListField


class Lab(Document):
    meta = {'collection': 'labs'}

    lab_id = StringField(required=True, unique=True, max_length=20)
    pc_count = IntField(required=True)
    location = StringField(required=True, max_length=50)
    name = StringField(required=True, max_length=100)
    accessibility = ListField(StringField(), default=[])
    installed_software = ListField(StringField(), default=[])

    def __repr__(self):
        return f"<Lab {self.name} located at {self.location}>"