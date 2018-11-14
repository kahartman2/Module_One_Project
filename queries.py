from models import *
from sqlalchemy import create_engine, func

engine = create_engine('sqlite:///nyc_restaurants.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_neighborhood_restaurants(neighborhood = 'Upper East Side'):
    name_list = []
    object_list = session.query(Restaurant).join(Neighborhood).filter(Neighborhood.name == neighborhood).all()
    for i in object_list:
        name_list.append(i.name)
    return name_list

#works
def return_cuisine(neighborhood):
    return session.query(Cuisine.name, func.count(Cuisine.restaurant_id)).join(Restaurant).join(Neighborhood).filter(Neighborhood.name == str(neighborhood)).group_by(Cuisine.name).all()


def ta_rating_avg_by_neighborhood():
    query_list = session.query(Neighborhood.name, func.avg(TripAdvisor.rating)).join(Restaurant).join(TripAdvisor).group_by(Neighborhood.name).order_by(func.avg(TripAdvisor.rating)).all()
    new_list = []
    for i in query_list:
        (x, y) = i
        y = round(y, 3)
        i = (x, y)
        new_list.append(i)
    return new_list

def inf_rating_avg_by_neighborhood():
    query_list = session.query(Neighborhood.name, func.avg(Infatuation.rating)).join(Restaurant).join(Infatuation).group_by(Neighborhood.name).order_by(func.avg(Infatuation.rating)).all()
    new_list = []
    for i in query_list:
        (x, y) = i
        y = round(y, 3)
        i = (x, y)
        new_list.append(i)
    return new_list

def inf_rating_avg_by_cuisine():
    query_list = session.query(Cuisine.name, func.avg(Infatuation.rating)).join(Restaurant).join(Infatuation).group_by(Cuisine.name).order_by(func.avg(Infatuation.rating)).all()
    new_list = []
    for i in query_list:
        (x, y) = i
        y = round(y, 3)
        i = (x, y)
        new_list.append(i)
    return new_list

def ta_rating_avg_by_cuisine():
    query_list = session.query(Cuisine.name, func.avg(TripAdvisor.rating)).join(Restaurant).join(TripAdvisor).group_by(Cuisine.name).order_by(func.avg(TripAdvisor.rating)).all()
    new_list = []
    for i in query_list:
        (x, y) = i
        y = round(y, 3)
        i = (x, y)
        new_list.append(i)
    return new_list

def mich_ratings_ta():
    return session.query(Restaurant.name, Michelin.stars, TripAdvisor.rating).join(Michelin).join(TripAdvisor).group_by(Restaurant.name).order_by(Restaurant.name).all()

def mich_ratings_inf():
    return session.query(Restaurant.name, Michelin.stars, Infatuation.rating).join(Michelin).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()

def mich_ratings(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    return session.query(Restaurant.name, Michelin.stars, TripAdvisor.rating, Infatuation.rating).join(Michelin).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()

def mich_stars_by_cuisine():
    return session.query(Cuisine.name, func.sum(Michelin.stars)).join(Restaurant).join(TripAdvisor).join(Michelin).group_by(Cuisine.name).all()

def mich_stars_by_cuisine1(star):
    return session.query(Cuisine.name, func.count(Michelin.stars)).join(Restaurant).join(TripAdvisor).join(Michelin).group_by(Cuisine.name).filter(Michelin.stars == star).all()

def mich_ratings(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    return session.query(Restaurant.name, Michelin.stars, TripAdvisor.rating, Infatuation.rating).join(Michelin).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
