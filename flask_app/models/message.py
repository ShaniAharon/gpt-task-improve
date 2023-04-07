from flask_app.database import db
from sqlalchemy.sql import func 

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role = db.Column(db.String(10)) 
    content = db.Column(db.String(500))  
    ts = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.relationship('User', back_populates='messages')

#The back_populates parameter tells SQLAlchemy
#  that the two relationships should be connected with each other.
#  This will allow you to access the related Message instances from a User instance
#  with the messages attribute,
#  and the related User instance from a Message instance with the user attribute.