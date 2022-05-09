import csv
import json

# we want to get to something that looks like this:

# {
#     "type": "FeatureCollection",
#     "features": [
#         {
#             "geometry": {
#                 "coordinates": [
#                     -151.5129,
#                     63.1016
#                 ],
#                 "type": "Point"
#             },
#             "properties": {
#                 "address": "xxxxx",
#                  "borough" : "xxxxx",
#                 "mag": 1,
#                 ... you could add other properties here that you want to display on the map
#             },
#             "type": "Feature"
#         }
#         ...
#     ]
# }


# so make the basic shape

geojson  = { "type": "FeatureCollection", "features": [] }


with open("Storefronts_Reported_Vacant_or_Not__Filing_Year_2020_-_2021_.csv",'r') as original_csv_file:
    reader = csv.DictReader(original_csv_file)
    for row in reader:
        #filter to show only storefronts that were reported vacant on 12/31/2021
        if row['VACANT ON 12/31'] == 'YES':

            # pull out the lat and long and convert them to floating point number, or decimal number, beause CSV is all string
            lat = float(row['LATITUDE'])
            lng = float(row['LONGITUDE'])

            # sometimes they are zero?
            if lat == 0 or lng == 0:
                # skip this one
                continue

            # make a basic feature
            # slot in the data points
            feature =  {
                "geometry": {
                    "coordinates": [
                        lng,
                        lat
                    ],
                    "type": "Point"
                },
                "properties": {
                    "address": row['PROPERTY STREET ADDRESS OR STOREFRONT ADDRESS'],
                     "borough" :  row['BOROUGH'],
                     "retail_type": row['PRIMARY BUSINESS ACTIVITY'],
                    # this is the property the earthquake heatmap example uses, so we'll just leave it at one
                    "mag": 1,
                },
                "type": "Feature"
            }

            # now add it to the features
            geojson['features'].append(feature)




# write it all out
json.dump(geojson,open('heat_map_2021.json','w'),indent=2)
