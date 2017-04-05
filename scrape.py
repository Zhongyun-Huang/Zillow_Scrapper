import requests
from bs4 import BeautifulSoup
import pandas as pd

def zillow_scraper(zipcode):
    # Make a property list for a zipcode
    property_list=[]
    count = 1
    url = "https://www.zillow.com/homes/"+zipcode +"_rb/"+ str(count) +'_p/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content) #make a soup for each url
    prop_info = soup.find_all("div",{"class":"zsg-photo-card-caption"})

    while soup.find_all("li", {'class':'zsg-pagination-next'}):
        #keep running the loop if there is a next bottom
        #Save all items in the new page to the property_list
        for item in prop_info:
            for i in item.find_all("span"):
                if i.get('class')==['zsg-photo-card-status']:
                    try: 
                        status = i.text
                    except:
                        status = 'NA'               
                if i.get('class')==['zsg-photo-card-price']:
                    try:
                        price = float(i.text.replace("$","").replace("/mo","").replace(",","").replace("+",""))
                    except:
                        price = 0.0
                if i.get('class')==['zsg-photo-card-info']:
                    info = i.text.replace("Studio","0.5 bd")
                    try:
                        bed = float(info.split()[0]) 
                    except:
                        bed = 0.0
                    try:
                        bath = float(info.split()[3])
                    except:
                        bath = 0.0
                    try:
                        size = float(info.split()[6].replace("--","0").replace("sqft","0").replace(",","").replace("+",""))
                    except:
                        size = 0.0
                if i.get('class')==['zsg-photo-card-address']:
                    try:
                        address = i.text
                    except:
                        address = ''
            prop=[status,price,bed,bath,size,address]
            property_list.append(prop)
        
        #Make a new soup if the next page exists    
        count = count + 1
        url = "https://www.zillow.com/homes/"+zipcode +"_rb/"+ str(count) +'_p/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content) #make a soup for each url
        prop_info = soup.find_all("div",{"class":"zsg-photo-card-caption"})
        
        labels = ['status','price','bed','bath','size','address']
        df = pd.DataFrame.from_records(property_list, columns = labels)

        return df