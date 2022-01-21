import pickle
import json
import numpy as np

__data_columns = None

def get_esitmated_price(Address, Bedroom, Bathroom, Den):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1