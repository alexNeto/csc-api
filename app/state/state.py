from csc import db


class State(db.Model):
    state_id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeingKey('country.country_id'))
    name = db.Column(db.String(128), index=True)
    english_name = db.Column(db.String(128), index=True)
    national_identifier = db.Column(db.String(64), index=True)
    abbreviation = db.Column(db.String(10), index=True)
    cities = db.relationship('City', backref='state', lazy='dynamic')
