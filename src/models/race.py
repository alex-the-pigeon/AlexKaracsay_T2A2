from init import db, ma
from marshmallow import fields

class Race(db.Model):
    __tablename__ = "races"
# this is specifying the data fields and the type of input eg integer, string(words) etc. The (50) refers to how many characters the input is limited to.
    id = db.Column(db.Integer, primary_key=True)
    race_name = db.Column(db.String(50))
    race_type = db.Column(db.String(50))
   
    rider_id = db.Column(db.Integer, db.ForeignKey('rider.id'), nullable=False) # this specifies the relationship FK to the riders table

    user = db.relationship('rider', back_populates='riders')

class RaceSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'race_name', 'race_type'])

    class Meta:
        fields = ('id', 'race_name', 'race_type',)
        ordered = True # this sets the order (as above) in which the data is dumped so it is consistent


race_schema = RaceSchema(many=True)