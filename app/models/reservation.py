from mongoengine import Document, StringField, DateTimeField, ReferenceField
from datetime import datetime

from app.models import Lab


class Reservation(Document):
    meta = {'collection': 'reservations'}

    reservation_id = StringField(required=True, unique=True, max_length=20)
    reason = StringField(required=True, max_length=50)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    status = StringField(choices=['reserved', 'canceled'], default='reserved')
    lab = ReferenceField(Lab, required=True)
    created_at = DateTimeField(default=datetime.utcnow())

    def __repr__(self):
        return f"<Reservation {self.reservation_id} for {self.reason} from {self.start_time} to {self.end_time}>"
