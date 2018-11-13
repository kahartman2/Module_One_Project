from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    address = Column(Text)
    zip_code = Column(Integer)
    cuisine = relationship('Cuisine', back_populates = 'restaurant')
    trip_advisor_info = relationship('TripAdvisor', back_populates='restaurant')
    infatuation_info = relationship('Infatuation', back_populates='restaurant')
    michelin_info = relationship('Michelin', back_populates='restaurant')
    neighborhood_id = Column(Integer, ForeignKey('neighborhoods.id'))
    neighborhood = relationship('Neighborhood', back_populates = 'restaurants')

class Cuisine(Base):
    __tablename__ = 'cuisines'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='cuisine')

class Neighborhood(Base):
    __tablename__ = 'neighborhoods'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    zip_code = Column(Integer)
    restaurants = relationship('Restaurant', back_populates = 'neighborhood')

class TripAdvisor(Base):
    __tablename__ = 'trip_advisor_info'

    id = Column(Integer, primary_key = True)
    price = Column(Integer)
    rating = Column(Integer)
    ranking = Column(Integer)
    number_reviews = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='trip_advisor_info')
    trip_advisor_breakdown = relationship('TripAdvisorBreakdown', back_populates='trip_advisor_info')

class TripAdvisorBreakdown(Base):
    __tablename__ = 'trip_advisor_breakdown'

    id = Column(Integer, primary_key = True)
    proportion_one_star = Column(Integer)
    proportion_two_star = Column(Integer)
    proportion_three_star = Column(Integer)
    proportion_four_star = Column(Integer)
    proportion_five_star = Column(Integer)
    trip_advisor_info_id = Column(Integer, ForeignKey('trip_advisor_info.id'))
    trip_advisor_info = relationship('TripAdvisor', back_populates='trip_advisor_breakdown')

class Infatuation(Base):
    __tablename__ = 'infatuation_info'

    id = Column(Integer, primary_key = True)
    price = Column(Integer)
    rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='infatuation_info')

class Michelin(Base):
    __tablename__ = 'michelin_info'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    stars = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='michelin_info')

engine = create_engine('sqlite:///nyc_restaurants.db')
Base.metadata.create_all(engine)

# relations matchup
    # neighborhood.restauarants
    # restaurant.neighborhood
