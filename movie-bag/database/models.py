import datetime
from dateutil.parser import parse
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')


class EventDetail(db.Document):
    bride_name = db.StringField(required=True, min_length=1, max_length=20)
    groom_name = db.StringField(required=True, min_length=1, max_length=20)
    mobile_no = db.StringField(required=True, min_length=10, max_length=10)
    event_date = db.DateTimeField(required=True)
    venue = db.StringField(required=True, min_length=1, max_length=20)
    venue_address = db.StringField(required=True, min_length=1, max_length=200)
    added_by = db.ReferenceField('User')
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    couple_image_id = db.IntField()


class CoupleImage(db.Document):
    image_id = db.IntField()
    image_name = db.StringField()
    image_data = db.FileField()


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))
    event_detail = db.ReferenceField('EventDetail', reverse_delete_rule=db.PULL)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Movie, 'added_by', db.CASCADE)
User.register_delete_rule(EventDetail, 'added_by', db.CASCADE)
