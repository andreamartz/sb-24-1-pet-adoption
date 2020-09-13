"""Pet Adoption model"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_PET_IMAGE_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, default=GENERIC_PET_IMAGE_URL)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)
