import csv
import pprint

vacant_zip = {}

pp = pprint.PrettyPrinter(indent=2)

with open("Storefronts_Reported_Vacant_or_Not__Filing_Year_2020_-_2021_.csv",'r') as original_csv_file:
    reader = csv.DictReader(original_csv_file)
    for row in reader:
        #filter to show only storefronts that were reported vacant on 12/31/2021
        if row['VACANT ON 12/31'] == 'YES':
            if "," not in row['POSTCODE']:
                zip_code_counter = row['POSTCODE']
                if zip_code_counter != '0':
                    if zip_code_counter not in vacant_zip:
                        vacant_zip[zip_code_counter]=0
                    vacant_zip[zip_code_counter]=vacant_zip[zip_code_counter]+1
                    #list of zip codes and number of vacant storefronts


pp.pprint(vacant_zip)
with open('vacant_zip.csv','w') as newcsvfile:
    header = ['Zip Code', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in vacant_zip.items():
        writer.writerow([key, value])
