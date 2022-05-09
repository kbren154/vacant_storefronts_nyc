# vacant_storefronts_nyc
Created for INFO 664 Programming for Cultural Heritage with Matt Miller at Pratt Institute, Spring 2022

I used NYC Open Data's Storefronts Reported Vacant or Not from the filing year 2019-2020 and 2020-2021 to determine if there was an increase in vacant storefronts across the city. I was specifically looking at the column - Vacant on 12/31.
I had planned to use pandas to merge the two files but found that an address could have multiple entries because it could have several units. The data didn't have any other identifying unit for each entry. Instead I worked with the dats years individually. 

First I created the code for vacant storefronts by zip code. The dataset includes a field for zip code, a field that was not always populated, and the field postal code which was entirely populated. 
 
  -vacant_zip_code_2021FINAL.py
  -vacant_zip_code_2020FINAL.py
  
There are also Tableau Vizzes for those generated csv files. 
  
  
