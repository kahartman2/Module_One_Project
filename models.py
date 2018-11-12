from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    neighborhood_id = Column(Integer, ForeignKey('neighborhoods.id'))
    cuisines = relationship('Cuisine', secondary = 'restaurants_cuisines')
    trip_advisor_info = relationship('TripAdvisor', back_populates='restaurant')
    infatuation_info = relationship('Infatuation', back_populates='restaurant')


class Cuisine(Base):
    __tablename__ = 'cuisines'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    restaurant = relationship('Restaurant', secondary = 'restaurants_cuisines')

class Neighborhood(Base):
    __tablename__ = 'neighborhoods'

    id = Column(Integer, primary_key = True)
    name = Column(Text)
    restaurant = relationship('Restaurant', back_populates = 'neighborhoods')

class TripAdvisor(Base):
    __tablename__ = 'trip_advisor_info'

    id = Column(Integer, primary_key = True)
    price = Column(Text)
    rating = Column(Integers)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', back_populates='trip_advisor_info')


class Infatuation(Base):
    __tablename__ = 'infatuation_info'

    id = Column(Integer, primary_key = True)
    price = Column(Text)
    rating = Column(Integers)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', back_populates='infatuation_info')

class RestaurantsCuisines(Base):
    __tablename__ = 'restaurants_cuisines'

    cuisine_id = Column(Integer, ForeignKey('cuisines.id'), primary_key = True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), primary_key = True)
