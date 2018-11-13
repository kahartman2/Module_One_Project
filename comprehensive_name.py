from ta_output import ta_with_zips
from infatuation_output import inf_list
from michelin_output import michelin_list

def get_names():
    name_list = []
    for i in ta_with_zips:
         if i['Name'] not in name_list:
             name_list.append(i['Name'])
    for i in inf_list:
         if i['Name'] not in name_list:
             name_list.append(i['Name'])

    for i in michelin_list:
        if i not in name_list:
            name_list.append(i)
    return name_list
