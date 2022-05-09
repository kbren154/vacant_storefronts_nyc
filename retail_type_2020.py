import csv
import pprint

retail_type = {}

pp = pprint.PrettyPrinter(indent=2)

with open("Storefronts_Reported_Vacant_or_Not__Filing_Year_2019_-_2020_.csv",'r') as original_csv_file:
    reader = csv.DictReader(original_csv_file)
    for row in reader:
        #filter to show only storefronts that were reported vacant on 12/31/2021
        if row['VACANT ON 12/31'] == 'YES':
            if "," not in row['PRIMARY BUSINESS ACTIVITY']:
                retail_type_counter = row['PRIMARY BUSINESS ACTIVITY']
                if retail_type_counter != None:
                    if retail_type_counter not in retail_type:
                        retail_type[retail_type_counter]=0
                    retail_type[retail_type_counter]=retail_type[retail_type_counter]+1
                    #list of retail types and number of vacant storefronts


pp.pprint(retail_type)
with open('retail_type_2020.csv','w') as newcsvfile:
    header = ['PRIMARY BUSINESS ACTIVITY', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in retail_type.items():
        writer.writerow([key, value])
