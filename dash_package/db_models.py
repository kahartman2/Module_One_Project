from dash_package import db

class Restaurant(db.Model):
    __tablename__ = 'nyc_restaurants'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    zip_code = db.Column(db.Integer)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    cuisine = db.relationship('Cuisine', back_populates = 'restaurant')
    trip_advisor_info = db.relationship('TripAdvisor', back_populates='restaurant')
    infatuation_info = db.relationship('Infatuation', back_populates='restaurant')
    michelin_info = db.relationship('Michelin', back_populates='restaurant')
    neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhoods.id'))
    neighborhood = db.relationship('Neighborhood', back_populates = 'restaurants')

class Cuisine(db.Model):
    __tablename__ = 'cuisines'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('nyc_restaurants.id'))
    restaurant = db.relationship('Restaurant', back_populates='cuisine')

class Neighborhood(db.Model):
    __tablename__ = 'neighborhoods'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    zip_code = db.Column(db.Integer)
    restaurants = db.relationship('Restaurant', back_populates = 'neighborhood')

class TripAdvisor(db.Model):
    __tablename__ = 'trip_advisor_info'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    number_reviews = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('nyc_restaurants.id'))
    restaurant = db.relationship('Restaurant', back_populates='trip_advisor_info')

class Infatuation(db.Model):
    __tablename__ = 'infatuation_info'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('nyc_restaurants.id'))
    restaurant = db.relationship('Restaurant', back_populates='infatuation_info')

class Michelin(db.Model):
    __tablename__ = 'michelin_info'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    stars = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('nyc_restaurants.id'))
    restaurant = db.relationship('Restaurant', back_populates='michelin_info')

db.create_all()
# __table_args__ = {'extend_existing': True}
