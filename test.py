# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:35:32 2018

@author: Lab 704
"""

from yelp.client import Client
import pdb
import pprint
import csv
from difflib import SequenceMatcher

MY_API_KEY = "zPdCbfiDxHWTB4-x6LHWGQgwU3cK7Jru-3egKk-r_G_P-XSzCFki5Jalq8WEdH0QwJPqNNY3V_SY39oESX0M4QXEqsiHqILD97rQtVsApIfuc4-p1VKbDx8KkJ_tW3Yx" #  Replace this with your real API key
def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')
        
def sort_by_distance(restaurants, location):
    '''
    restaurants[LIST]: list of restaurants
    location[STRING]: ref location to search
    '''
    result = {}
    client = Client(MY_API_KEY)
    loc = False
    for each in restaurants:
        try:
            x = client.business.search_by_keyword(term=each,location=location)
            try:
                info = x['businesses'][0]
            except:
                print('{}: nothing returned'.format(each))
            name = info['name']
            dist = info['distance']
            if not loc:
                print("location: {}".format(x['region']))
                loc = True
    #        price = info['price']
            result[name] = dist
            if SequenceMatcher(None,each,name).ratio() < 0.7:
                print('-----')
                print("{} --> {}".format(each,name))
                print(">possible names:")
                for i in x['businesses'][:3]:
                    print( i['name'])
                print('-----')
        except Exception as e:
            print(e)
            #pdb.set_trace()
        
    print("LOOP 1 FINIHSED")
#    for key, value in sorted(result.iteritems(), key=lambda (k,v): (v,k)):
#        print "%s: %s" % (key, value) 
    return result

if __name__ == "__main__":
    restaurants = []
    with open('names.csv','rt') as csvfile:
        reader = csv.reader(csvfile)#, delimiter=' ', quotechar='|')
        for each in reader:
            restaurants.append(each[0])
    val = sort_by_distance(restaurants, '107 Grand Street')
    
'''To be added in business.py

from yelp.config import BUSINESS_PATH, SEARCH_PATH
    def search_by_keyword(self, **url_params):
        """Comments here

        """
        business_path = SEARCH_PATH
#        print(url_params)
        response = self.client._make_request(business_path, url_params=url_params)
#        print(response)
        return response
'''