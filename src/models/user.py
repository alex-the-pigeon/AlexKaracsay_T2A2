from init import db, ma
from marshmallow import fields

# creating class and naming table
class User(db.Model):
    __tablename__ = 'users'
# table attributes
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    riders = db.relationship('Rider', back_populates='user') 
    

# this shows the fields we want to convert to JSON for the front end
class UserSchema(ma.Schema):
    riders = fields.List(fields.Nested('RiderSchema', exclude=['user'])) # specifying which schema this relates to 

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'is_admin', 'riders')

# specifying one user and many users, excluding user password from being sent to front end for security
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])