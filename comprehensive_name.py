from geocode import add_lat_long
from infatuation_output import inf_list
from convert_to_dictionary import mich_dict

def get_names():
    name_list = []
    filter_list = []
    for i in add_lat_long():
        name_list.append({'Name': i['Name'], 'Address': i['Address'], 'Zip': i['Zip'], 'Latitude': i['Latitude'], 'Longitude': i['Longitude']})
    for i in name_list:
        filter_list.append(i['Name'])
    for i in inf_list:
         if i['Name'] not in filter_list:
             name_list.append({'Name': i['Name'], 'Address':' ' , 'Zip': ' ', 'Latitude': ' ', 'Longitude': ' '})
    for i in name_list:
        filter_list.append(i['Name'])
    for i in mich_dict:
        if i['Name'] not in filter_list:
            name_list.append({'Name': i['Name'], 'Address': ' ',  'Zip': ' ', 'Latitude': ' ', 'Longitude': ' '})
    return name_list
