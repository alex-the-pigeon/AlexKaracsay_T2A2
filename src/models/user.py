from init import db, ma

# creating class and naming table
class User(db.Model):
    __tablename__ = 'user'
# table attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

# this shows the fields we want to convert to JSON for the front end
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

# specifying one user and many users, excluding user password from being sent to front end for security
user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])