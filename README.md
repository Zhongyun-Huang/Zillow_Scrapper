# Zillow_by_Zipcode
* Zillow_by_Zipcode is a tool built for users to extract property information from a zipcode area, and make wise decisions on which property to rent or to buy. 
* It also enables users to compare affordability and community information between zipcodes. They can also decide on whether to rent or to buy properties from an area
* This tool can also be used to study social-economic status across the country by area


## Input
Two zipcodes

## Output
* A table to compare between two zipcodes 

|  Zipcodes     | 02148         | 02420  |
| ------------- |:-------------:| ------:|
| mean_size     | 884.11 | 2583.12 |
| mean_bed      | 1.79   |3.63|
| mean_price_per_sqft | 478.54    | 731.86 |
| mean_price_per_bd | 41598.1  |  219055 |
| mean_rent | 11949   | 3189 |
| rent_vs_buy | 0.03  |  0 |


## Usage
* Go to terminal, run "python zipcode.py"
* Follow instructions on the screen: "Please enter your two zipcodes for comparison (separated by a comma): "
* The scrape.py will be called by the zipcode.py to extract real-time property information on Zillow. 





