import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # data converted into dictionary.

all_eq_dicts = all_eq_data['features']

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

location = []
for eq_dict in all_eq_dicts:
    coord = (eq_dict['geometry']['coordinates'][0], 
        eq_dict['geometry']['coordinates'][1])
    location.append(coord)

print(location[:10])