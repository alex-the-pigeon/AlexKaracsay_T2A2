from init import db, ma

# creating class and naming table
class User(db.Model):
    __tablename__ = 'user'
# table attributes !!! having issues when trying to seed table. sqlalchemy.exc.DataError: (psycopg2.errors.StringDataRightTruncation) value too long for type character varying(50)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# this shows the fields we want to convert to JSON for the front end
class UserSchema(ma.Schema):
    riders = fields.List(fields.Nested('RiderSchema', exclude=['user'])) # specifying which schema this relates to 

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'is_admin', 'riders')

# specifying one user and many users, excluding user password from being sent to front end for security
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])