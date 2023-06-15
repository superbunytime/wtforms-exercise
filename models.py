from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://cdn.discordapp.com/attachments/1030335903253663744/1116788294743760916/image.png"

db = SQLAlchemy()


class Pet(db.Model):
    """Adoptable pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return either default or linked image for pet"""

        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """Copy-pasted from every other flask app I've worked on"""

    db.app = app
    db.init_app(app)