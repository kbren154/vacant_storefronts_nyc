# vacant_storefronts_nyc
Created for INFO 664 Programming for Cultural Heritage with Matt Miller at Pratt Institute, Spring 2022

I used NYC Open Data's Storefronts Reported Vacant or Not from the filing year 2019-2020 and 2020-2021 to determine if there was an increase in vacant storefronts across the city. I was specifically looking at the column - Vacant on 12/31. 

--------------
I had planned to use pandas to merge the two files but found that an address could have multiple entries because it could have several units. The data didn't have any other identifying unit for each entry. Instead I worked with the data years individually.

--------------
First I created the code for vacant storefronts by zip code. The dataset includes a field for zip code, a field that was not always populated, and the field postal code which was entirely populated. 
 
  -vacant_zip_code_2021FINAL.py
  -vacant_zip_code_2020FINAL.py
  
There are also Tableau Vizzes for those generated csv files. 
For 2021: https://public.tableau.com/views/VacantStorefrontsbyZipCode/Sheet1?:language=en-US&:display_count=n&:origin=viz_share_link
For 2020: https://public.tableau.com/views/VacantStorefrontsbyZipCodes2021/VacantStorefrontZipCodes2021?:language=en-US&:display_count=n&:origin=viz_share_link

--------------
Next heat map codes were created to determine the greatest concentration of empty storefronts. This code was modeled to work with geojson.io. When the python code is run a json file can be used to populate the map. 
		
		-heat_map_2021.py
		-heat_map_2020.py
		
--------------
Lastly a code was run to create the visualizations of vacant storefronts based on primary business activity. I thought this could inform what types of businesses were struggling due to the pandemic. Unfortunately a majority of the vacant storefronts did not have a retail type listed - NO BUSINESS ACTIVITY IDENTIFIED. Without knowing what this term means, it is not defined on the dataset page it is difficult to make any conclusions. A copy of the codes are included. 
		
		-retail_type_2021.py
		-retail_type_2020.py

