import requests
import pandas as pd
from scrape import zip_dataframe
import seaborn as sns
import matplotlib.pyplot as plt
import re

''' To improve
    (1) when there is nothing on list for a zipcode
    (2) how to avoid the problem of "local variable called before assigned)
    (3) use regular expression to grab everything for rent, everything for sale
'''



class RegionStat(object):
    ''' This is a class to contain all property information from the same zipcode area
        Methods include: (1)  price: mean_for_sale, mean_for_rent
                         (2)  no. beds: mean
                         (3)  no. baths: mean
                         (4)  size: mean, min, max
                         (5)  ave price_per_sqft
                         (6)  ave price_per_bed
    '''
    def __init__(self, zipcode):
        self.df = zip_dataframe(zipcode)
        #self.feature = '' # enter: 'bed', 'bath', 'size', 'price'
        #self.stat = ''  # enter: 'mean', 'min', 'max'

    def for_sale(self):
        for_sale = self.df[self.df['status'].str.contains("Sale")]
        return for_sale

    def for_rent(self):
        #for_rent = self.df[re.match("Rent",self.df.status)
        for_rent = self.df[self.df['status'].str.contains("Rent")]
        return for_rent

    def mean_bed(self):
        mean_bed = self.df.describe()['bed']['mean']
        return round(mean_bed,2)

    def mean_bath(self):
        mean_bath = self.df.describe()['bath']['mean']
        return str(round(mean_bath,2))

    def mean_size(self):
        try:
            mean_size = self.df.describe()['size']['mean']
            return round(mean_size,2)
        except:
            return "No property on list"

    def mean_price_sale(self):
        mean_price_sale = int(self.for_sale().describe()['price']['mean'])
        return round(mean_price_sale,2)

    def mean_price_rent(self):
        mean_price_rent = int(self.for_rent().describe()['price']['mean'])
        return round(mean_price_rent,2)


    def mean_price_per_sqft_sale(self):
        #mean_price_per_sqft = int(self.df[re.match("Sale",self.df.status)].describe()['price']['mean']) \
        #    / self.df.describe()['size']['mean']
        mean_price_per_sqft_sale = (self.mean_price_sale())/(self.mean_size())
        return str(round(mean_price_per_sqft_sale,2))


    def mean_price_per_bed(self):
        mean_price_per_bed = int(self.df.describe()['price']['mean'])\
        /self.df.describe()['bed']['mean']
        return round(mean_price_per_bed,2)

    def rent_vs_buy(self):
        rent_vs_buy = (self.mean_price_rent())/(self.mean_price_sale())
        return round(rent_vs_buy,2)

def main():
    zips = raw_input("Please enter your two zipcodes for comparison (separated by a comma): ")
    zip = zips.split(',')
    rs1 = RegionStat(zip[0])
    rs2 = RegionStat(zip[1])
    rowname = ['mean_size','mean_bed','mean_price_per_sqft','mean_price_per_bd','mean_rent','rent_vs_buy']
    zip_frame = pd.DataFrame(
                         {zip[0]: [rs1.mean_size(),\
                            rs1.mean_bed(),\
                            rs1.mean_price_per_sqft_sale(),\
                            rs1.mean_price_per_bed(),\
                            rs1.mean_price_rent(),\
                            rs1.rent_vs_buy()],\
                          zip[1]: [rs2.mean_size(),\
                            rs2.mean_bed(),\
                            rs2.mean_price_per_sqft_sale(),\
                            rs2.mean_price_per_bed(),\
                            rs2.mean_price_rent(),\
                            rs2.rent_vs_buy()]}
                        )
    zip_frame.index = rowname
    print zip_frame
    #print "The zipcode you entered is %s " %zip[0],
    #print "The mean size of properties is %s" %str(rs1.mean_size())
    #print "The mean no. of bedrooms is %s" %str(rs1.mean_bed())
    #print "The mean PRICE FOR RENT is %s" %str(rs1.mean_price_rent())
    #print "The mean PRICE FOR SALE is %s" %str(rs1.mean_price_sale())
    #print "The mean price per sqft FOR SALE is %s" %str(rs1.mean_price_per_sqft_sale())
    #print "The mean price per bedroom is %s" %str(rs1.mean_price_per_bed())

if __name__ == "__main__":
    main()