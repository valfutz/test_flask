from datetime import datetime, timedelta
from time import strftime

from sqlalchemy import ForeignKey

from app.database import db



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    created_by = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    creator = db.relationship("User", foreign_keys=[created_by])
    # registrations = db.relationship('EventUser', backref='event')

    begin_at = db.Column(db.String(length=255), nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    end_at = db.Column(db.String(length=255), nullable=False, default=(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"))

    max_users = db.Column(db.Integer, nullable=False, default=1)
    is_active = db.Column(db.Boolean, nullable=False, default=True)


    def __repr__(self):
        return f'<Event {self.id}: {self.title}>'

class EventUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    event_id = db.Column(db.Integer, ForeignKey('event.id'))
    created_at = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', foreign_keys=[user_id])
    event = db.relationship('Event', foreign_keys=[event_id])

    def __repr__(self):
        return f'<Event {self.user_id}: {self.event_id}>'