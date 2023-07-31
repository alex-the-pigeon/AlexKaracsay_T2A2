from init import db, ma
from marshmallow import fields

class Safety(db.Model):
    __tablename__ = "safety"
# this is specifying the data fields and the type of input eg integer, string(words) etc. The (50) refers to how many characters the input is limited to.
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(50))
    contact_phone = db.Column(db.String(50))
    relationship = db.Column(db.String(50))
   
    rider_id = db.Column(db.Integer, db.ForeignKey('rider.id'), nullable=False) # this specifies the relationship FK to the riders table

    user = db.relationship('rider', back_populates='riders')

class Safetychema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'contact_name', 'contact_phone', 'relationship'])

    class Meta:
        fields = ('id', 'contact_name', 'contact_phone', 'relationship')
        ordered = True # this sets the order (as above) in which the data is dumped so it is consistent

safety_schema = SafetySchema(many=True)