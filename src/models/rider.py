from init import db, ma
from marshmallow import fields

class Rider(db.Model):
    __tablename__ = "riders"
# this is specifying the data fields and the type of input eg integer, string(words) etc. The (50) refers to how many characters the input is limited to.
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    age = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # this specifies the relationship FK to the users table

    user = db.relationship('User', back_populates='riders')

class RiderSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'username', 'email', 'password', 'is_admin'])

    class Meta:
        fields = ('id', 'last_name', 'first_name', 'sex', 'age')
        ordered = True # this sets the order (as above) in which the data is dumped so it is consistent

rider_schema = RiderSchema()
riders_schema = RiderSchema(many=True)


