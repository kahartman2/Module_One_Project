from trip_advisor_output import trip_advisor_output
from infatuation_output import infatuation_output
from fuzzywuzzy import fuzz, process
from michelin_updated import mich_list
from overlap_list import overlap_ta_infat

ta_plus_infatuation = trip_advisor_output + infatuation_output

zips = []

for element in trip_advisor_output:
    if element['Address'][-5] == '-':
        zips.append(int(element['Address'][-10:-5]))
    else:
        try:
            zips.append(int(element['Address'][-5:]))
        except ValueError:
            zips.append(int(00000))

ta_with_zips = trip_advisor_output.copy()
index = 0
for element in ta_with_zips:
    ta_with_zips[index]['Zip'] = zips[index]
    index += 1

ta_names = []
for element in trip_advisor_output:
    ta_names.append(element['Name'])

i_names = []
for element in infatuation_output:
    i_names.append(element['Name'])

overlap = set(ta_names).intersection(i_names)

if name in overlap:
