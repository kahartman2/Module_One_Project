import csv
from ta_output import ta_with_zips
from convert_to_dictionary import address_dict
from queries import get_name_address

def extract_address():
    address_list = []
    for i in ta_with_zips:
        address_list.append({'Name': i['Name'], 'Address': i['Address']})
    with open('address_list2.csv', mode='w') as address_file:
        address_writer = csv.writer(address_file, delimiter=',')
        for i in address_list:
            address_writer.writerow([i])

def lat_lon_ta():
    new_list = []
    for i in address_dict:
        new_list.append({'Name': i['Name'], 'Latitude': i['Latitude'], 'Longitude': i['Longitude']})
    return new_list

def add_lat_long():
    index = 0
    for item in ta_with_zips:
        item['Latitude'] = ' '
        item['Longitude'] = ' '
    for item in lat_lon_ta():
        if ta_with_zips[index]['Name'] == item['Name']:
            ta_with_zips[index]['Latitude'] = item['Latitude']
            ta_with_zips[index]['Longitude'] = item['Longitude']
        index +=1
    return ta_with_zips
