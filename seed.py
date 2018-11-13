
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Restaurant, Address, Cuisine, Neighborhood, TripAdvisor, TripAdvisorBreakdown, Infatuation, Michelin, RestaurantsCuisines, engine
from comprehensive_name import get_names
from infatuation_output import inf_list
from ta_output import ta_with_zips
from michelin_output import michelin_list

comprehensive_name_list = get_names()

full_infatuation_list =  inf_list

full_tripadvisor_list = ta_with_zips

full_michelin_list = michelin_list

neighborhoods = [{'Name': 'Lower Eaast Side', 'Zip': 10012}, {'Name': 'Bushwick', 'Zip': 10027},  {'Name': 'UWS', 'Zip': 10038}, {'Name': 'UWS', 'Zip': 10003}]

Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

session = session()

def add_restaurant():
    for item in comprehensive_name_list:
        restaurant = Restaurant(name = item)
        session.add(restaurant)
        session.commit()

def add_inf():
    r = session.query(Restaurant).all()
    for i in r:
        for inf_item in full_infatuation_list:
            if i.name == inf_item['Name']:
                i.infatuation_info = [Infatuation(price = inf_item['Price'], rating = inf_item['Rating'])]
                session.add(i)
                session.commit()

def add_ta():
    r = session.query(Restaurant).all()
    for i in r:
        for ta_item in full_tripadvisor_list:
            if i.name == ta_item['Name']:
                i.trip_advisor_info = [TripAdvisor(price = ta_item['Price'], rating = ta_item['Rating'], ranking = ta_item['Ranking'], number_reviews = ta_item['Number of Reviews'])]
                session.add(i)
                session.commit()

def add_mi():
    r = session.query(Restaurant).all()
    for i in r:
        for mi_item in full_michelin_list:
            if i.name == mi_item:
                session.add(i)
                session.commit()

def add_neighborhood():
    for item in neighborhoods:
        neighborhood = Neighborhood(name = item['Name'], zip_code = item['Zip'])
        session.add(neighborhood)
        session.commit()

def add_address():
    r = session.query(Restaurant).all()
    for i in r:
        for ta_item in full_tripadvisor_list:
            if i.name == ta_item['Name']:
                i.address = [Address(address = ta_item['Address'], zip_code = ta_item['Zip'])]
                session.add(i)
                session.commit()

def add_neighborhood_id():
    r = session.query(Address).all()
    s = session.query(Neighborhood).all()
    for i in r:
        for j in s:
            if i.zip_code == j.zip_code:
                i.neighborhood_id = j.id
                session.add(i)
                session.commit()

def add_cuisine():
    r = session.query(Restaurant).all()
    for i in r:
        for ta_item in full_tripadvisor_list:
            if i.name == ta_item['Name'] and ta_item['Cuisines'] != None:
                # try:
                i.cuisine = [Cuisine(name = ta_item['Cuisines'][0])]
                # except TypeError:
                #     i.cuisine = []
    session.add(i)
    session.commit()
