from csc import db


class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeingKey('state.state_id'))
    name = db.Column(db.String(128), index=True)
    english_name = db.Column(db.String(128), index=True)
    national_identifier = db.Column(db.String(64), index=True)
