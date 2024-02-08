from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, it's a security breach
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('favorites', lazy=True))

    def __repr__(self):
        return f'<Favorite {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id
        }

class Exhibits(db.Model):
    __tablename__ = 'exhibits'
    id = db.Column(db.Integer, primary_key=True)
    exhibit_name = db.Column(db.String(250), nullable=False)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))
    favorite = db.relationship('Favorite', backref=db.backref('exhibits', lazy=True)) 

    def __repr__(self):
        return f'<Exhibit {self.exhibit_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "exhibit_name": self.exhibit_name,
            "favorite_id": self.favorite_id,
        }
    
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)
    death_year = db.Column(db.Integer, nullable=True)
    nationality = db.Column(db.String(100), nullable=True)

    exhibits = db.relationship('Exhibit', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "death_year": self.death_year,
            "nationality": self.nationality,
        }



