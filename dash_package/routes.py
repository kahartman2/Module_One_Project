from flask import render_template
from dash_package import server, app
from dash_package.db_models import Restaurant


@server.route('/nyc_restaurants')
def render_restaurants():
    return "Hello world"

'''
    nycrestaurant = Restaurant.query.get(1)
    return 'nycrestaurant.name'
'''
