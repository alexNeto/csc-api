from csc import db


class Country(db.Model):
    country_id = db.Column(db.Integer, primary_key=True)
    english_name = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True)
    iso3 = db.Column(db.String(3), index=True)
    iso2 = db.Column(db.String(2), index=True)
    phone_code = db.Column(db.String(3), index=True)
    capital = db.Column(db.String(128), index=True)
    currency = db.Column(db.String(64), index=True)
    states = db.relationship('State', backref='country', lazy='dynamic')
