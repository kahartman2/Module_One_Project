from models import *
from sqlalchemy import create_engine, func

engine = create_engine('sqlite:///nyc_restaurants.db')

Session = sessionmaker(bind=engine)
session = Session()

#chart 1
def inf_vs_ta_ratings(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    return session.query(Restaurant.name, TripAdvisor.rating, Infatuation.rating).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()

#chart2
def rating_box_whisker(neighborhood):
    return session.query(Restaurant.name, TripAdvisor.rating, Infatuation.rating).join(TripAdvisor).join(Infatuation).join(Neighborhood).filter(Neighborhood.name == neighborhood).all()
#chart2
def price_box_whisker():
    return session.query(Restaurant.name, Neighborhood.name, TripAdvisor.price, Infatuation.price).join(Restaurant).join(TripAdvisor).join(Infatuation).group_by(Neighborhood.name).all()
