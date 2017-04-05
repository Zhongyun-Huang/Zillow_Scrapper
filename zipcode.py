import requests
import pandas as pd

from scrape import zillow_scraper

class RegionStat(object):
    ''' This is a class to contain all property information from the same zipcode area 
        Methods include: (1)  price: mean, min, max
                         (2)  no. beds: mean
                         (3)  no. baths: mean
                         (4)  size: mean, min, max
                         (5)  ave price_per_sqft
                         (6)  ave price_per_bed
    '''
    def __init__(self, zipcode):  
        self.df = zillow_scraper(zipcode)
        #self.feature = '' # enter: 'bed', 'bath', 'size', 'price'
        #self.stat = ''  # enter: 'mean', 'min', 'max'
    
    def mean_bed(self):
        mean_bed = self.df.describe()['bed']['mean']
        return mean_bed
    
    def mean_bath(self):
        mean_bath = self.df.describe()['bath']['mean']
        return mean_bath
        
    
    def mean_size(self):
        mean_size = self.df.describe()['size']['mean']
        return mean_size
    
    def mean_price(self):
        mean_price = int(self.df.describe()['price']['mean'])
        return mean_price
    
    def mean_price_per_sqft(self):
        mean_price_per_sqft = int(self.df.describe()['price']['mean'])/self.df.describe()['size']['mean']
        return mean_price_per_sqft
    
    def mean_price_per_bed(self):
        mean_price_per_bed = int(self.df.describe()['price']['mean'])/self.df.describe()['bed']['mean']
        return mean_price_per_bed

if __name__ == "__main__":
    zip = raw_input("Please enter your zipcode: ")
    rs = RegionStat(zip)
    print "The zipcode you entered is %s" %zip
    print "The mean price per sqft is %s\n" %str(rs.mean_price_per_sqft())
    print "The mean size of properties is %s" %str(rs.mean_size())