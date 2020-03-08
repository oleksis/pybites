from collections import Counter
#from json import loads

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

#with open("cars.json", "r") as file:
#    data = loads(file.read())

# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    c = Counter([car["automaker"] 
                 for car in data 
                 if car["year"] == year]).most_common()
    mpa = max(c, key=lambda x: x[1])
    return mpa[0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    c = Counter([car["model"] 
                 for car in data 
                 if car["automaker"] == automaker 
                 and car["year"] == year])
    return set(c.keys())
