
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Restaurant, Address, Cuisine, Neighborhood, TripAdvisor, TripAdvisorBreakdown, Infatuation, Michelin, RestaurantsCuisines, engine
# from infatuation_cleaner import full_infatuation_list

comprehensive_name_list = [{'Name': 'R1'}, {'Name': 'R2'}, {'Name': 'R3'}, {'Name': 'R4'}, {'Name': 'R5'}]

full_infatuation_list = [{'Name': 'R3', 'Neighborhood': 'Lower East Side', 'Rating': '8.0', 'Price': '2'}, {'Name': 'R1', 'Neighborhood': 'Bushwick', 'Rating': '9.3', 'Price': '4'}, {'Name': 'R4', 'Neighborhood': 'Nolita', 'Rating': '8.0', 'Price': '3'}, {'Name': 'R5', 'Neighborhood': 'Lower East Side', 'Rating': '8.2', 'Price': '3'}]

full_tripadvisor_list = [{'Name': 'R4', 'Ranking': 1, 'Rating': 4.5, 'Number of Reviews': 537, 'Address': '184 Prince St New York City, NY 10012-2979', 'Zip': 10012, 'Cuisines': ['Italian', ' Vegetarian Friendly', ' Vegan Options'], 'Price': '$$ - $$$', 'Rating Types': {'5-Star': 74, '4-Star': 20, '3-Star': 4, '2-Star': 1, '1-Star': 1}}, {'Name': 'R3', 'Ranking': 2, 'Rating': 4.5, 'Number of Reviews': 867, 'Address': '97 Nassau St New York City, NY 10038-2703', 'Zip': 10038, 'Cuisines': ['Italian', ' Fast Food', ' Vegetarian Friendly'], 'Price': '$', 'Rating Types': {'5-Star': 79, '4-Star': 15, '3-Star': 4, '2-Star': 1, '1-Star': 1}}, {'Name': 'R1', 'Ranking': 3, 'Rating': 5.0, 'Number of Reviews': 344, 'Address': '225 Park Ave S New York City, NY 10003-1604', 'Zip':10003, 'Cuisines': ['French', ' Steakhouse', ' Gluten Free Options'], 'Price': '$$$$', 'Rating Types': {'5-Star': 89, '4-Star': 7, '3-Star': 2, '2-Star': 1, '1-Star': 1}}, {'Name': 'R2', 'Ranking': 4, 'Rating': 5.0, 'Number of Reviews': 278, 'Address': '227 Lenox Ave New York City, NY 10027-6542', 'Zip': 10027 ,'Cuisines': ['Pizza', ' Vegetarian Friendly', ' Vegan Options'], 'Price': '$$ - $$$', 'Rating Types': {'5-Star': 81, '4-Star': 17, '3-Star': 1, '2-Star': 0, '1-Star': 1}}]

full_michelin_list = [{'Name': 'R2', 'Star': 'One'}, {'Name': 'R3', 'Star': 'Three'}, {'Name': 'R1', 'Star': 'Three'}]

neighborhoods = [{'Name': 'Lower Eaast Side', 'Zip': 10012}, {'Name': 'Bushwick', 'Zip': 10027},  {'Name': 'UWS', 'Zip': 10038}, {'Name': 'UWS', 'Zip': 10003}]

Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

session = session()

def add_restaurant():
    for item in comprehensive_name_list:
        restaurant = Restaurant(name = item['Name'])
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
            if i.name == mi_item['Name']:
                i.michelin_info = [Michelin(rating = mi_item['Star'])]
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
