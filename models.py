from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), unique=False, nullable=False)
    text = db.Column(db.Text, unique=False, nullable=False)
    time = db.Column(db.Text, unique=False, nullable=False)


    def __repr__(self):
        return f'{self.name} - {self.text}'
