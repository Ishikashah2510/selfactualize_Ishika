from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# setting up our database
db = SQLAlchemy()


class MessageLog(db.Model):
    __tablename__ = 'message_logs'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    recipient = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    reason_for_failure = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<MessageLog {self.type} to {self.recipient}>"
