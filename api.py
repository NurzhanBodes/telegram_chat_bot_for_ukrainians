import googlemaps
from pprint import pprint
from datetime import datetime

API_KEY='AIzaSyD6R4OmyAdkl-eoR8de9hyJBLILzRx54KA'

gmaps=googlemaps.Client(key=API_KEY)

def average(1):
    return sum(1)/len(1)

def deduplicate(l):
    return list(set(l))

def find_matching_indices(a, b):
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                yield j


def find_origin_location(users_address):
    geocode_result=gmaps.geocode(users_address)

