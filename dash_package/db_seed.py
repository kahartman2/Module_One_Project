from __init__.py import *
from mod_files.ta_output import ta_with_zips
from mod_files.comprehensive_name import get_names
from mod_files.infatuation_output import inf_list
from mod_files.convert_to_dictionary import mich_dict, zip_dict

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite:///nyc_restaurants.db')
#
# Session = sessionmaker(bind=engine)
# session = Session()

comprehensive_name_list = get_names()
full_infatuation_list =  inf_list
full_tripadvisor_list = ta_with_zips
full_michelin_list = mich_dict
neighborhoods =  zip_dict

def add_restaurant():
    for item in comprehensive_name_list:
        restaurant = Restaurant(name = item['Name'], address = item['Address'], zip_code = item['Zip'], latitude = item['Latitude'], longitude = item['Longitude'])
        db.session.add(restaurant)
        db.session.commit()

def add_inf():
    r = db.session.query(Restaurant).all()
    for i in r:
        for inf_item in full_infatuation_list:
            if i.name == inf_item['Name']:
                i.infatuation_info = [Infatuation(price = inf_item['Price'], rating = inf_item['Rating'])]
                db.session.add(i)
                db.session.commit()

def add_ta():
    r = db.session.query(Restaurant).all()
    for i in r:
        for ta_item in full_tripadvisor_list:
            if i.name == ta_item['Name']:
                i.trip_advisor_info = [TripAdvisor(price = ta_item['Price'], rating = ta_item['Rating'], ranking = ta_item['Ranking'], number_reviews = ta_item['Number of Reviews'])]
                db.session.add(i)
                db.session.commit()

def add_mi():
    r = db.session.query(Restaurant).all()
    for i in r:
        for mi_item in mich_dict:
            if i.name == mi_item['Name']:
                i.michelin_info = [Michelin(name = mi_item['Name'], stars = mi_item['Stars'])]
                db.session.add(i)
                db.session.commit()

def add_neighborhood():
    for item in neighborhoods:
        neighborhood = Neighborhood(name = item['Neighborhood'], zip_code = item['Zip'])
        db.session.add(neighborhood)
        db.session.commit()

def add_neighborhood_id():
    r = db.session.query(Restaurant).all()
    s = db.session.query(Neighborhood).all()
    for i in r:
        for j in s:
            if i.zip_code == j.zip_code:
                i.neighborhood_id = j.id
                db.session.add(i)
                db.session.commit()


def add_neighborhood_id():
    r = db.session.query(Restaurant).all()
    s = db.session.query(Neighborhood).all()
    for j in s:
        for i in r:
            if i.zip_code == j.zip_code:
                i.neighborhood_id = j.id
                db.session.add(i)
                db.session.commit()

def add_cuisine():
    r = db.session.query(Restaurant).all()
    for i in r:
        for ta_item in full_tripadvisor_list:
            if i.name == ta_item['Name'] and ta_item['Cuisines'] != None:
                i.cuisine = [Cuisine(name = ta_item['Cuisines'][0])]
    db.session.add(i)
    db.session.commit()

add_restaurant()
add_inf()
add_ta()
add_mi()
add_neighborhood()
add_cuisine()
add_neighborhood_id()
