from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    Name = db.Column(db.String(64), index=True, unique=False)
    PatronymicName = db.Column(db.String(64), index=True, unique=False)
    SurName = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)