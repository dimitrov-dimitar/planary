from db import db


class PlantModel(db.Model):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    latin_name = db.Column(db.String(120), nullable=False)
    catalogue_name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(240), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("UserModel")


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # plants = db.relationship("PlantModel", backref="plants", lazy="dynamic")
    # demo = db.Column(db.String(20), nullable=False)


# class AdminModel(db.Model):
#     __tablename__ = "admins"

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255), nullable=False)
#     last_name = db.Column(db.String(255), nullable=False)

