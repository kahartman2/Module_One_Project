
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Restaurant, Cuisine, Neighborhood, TripAdvisor, TripAdvisorBreakdown, Infatuation, Michelin, engine
from comprehensive_name import get_names
from infatuation_output import inf_list
from ta_output import ta_with_zips
from michelin_output import michelin_list
from convert_to_dictionary import mich_dict, zip_dict

comprehensive_name_list = get_names()

full_infatuation_list =  inf_list

full_tripadvisor_list = ta_with_zips

full_michelin_list = mich_dict

neighborhoods =  zip_dict

Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

session = session()

def add_restaurant():
    for item in comprehensive_name_list:
        restaurant = Restaurant(name = item['Name'], address = item['Address'], zip_code = item['Zip'])
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
        for mi_item in mich_dict:
            if i.name == mi_item['Name']:
                i.michelin_info = [Michelin(name = mi_item['Name'], stars = mi_item['Stars'])]
                session.add(i)
                session.commit()

def add_neighborhood():
    for item in neighborhoods:
        neighborhood = Neighborhood(name = item['Neighborhood'], zip_code = item['Zip'])
        session.add(neighborhood)
        session.commit()

def add_neighborhood_id():
    r = session.query(Restaurant).all()
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
                i.cuisine = [Cuisine(name = ta_item['Cuisines'][0])]
    session.add(i)
    session.commit()
