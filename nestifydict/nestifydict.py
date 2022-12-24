"""
This module contains functions for restructuring and extracting information from nested dictionaries
"""
__license__ = "BSD-3"
__docformat__ = 'reStructuredText'
__author__ = "Jared Beard"

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from copy import deepcopy

__all__ = ["merge", "unstructure","structure"]

def merge(d_default : dict, d_merge : dict):
    """
    Adds d_merge values to d_default recursively. 
    Values in d_merge overwrite those of d_default values, 
    however nonexistent values in d_default are retained, 
    which differs from use of {**d_base, **d_merge}

    :param d_default: (dict) base dictionary
    :param d_merge: (dict) dictionary to add
    :return: (dict) combined dictionary
    """
    d_default = deepcopy(d_default)

    for key, val in d_merge:
        if key not in d_default or (not isinstance(d_default[key], dict)):
            d_default[key] = deepcopy(val)
        else:
            d_default[key] = merge(d_default[key], d_merge[key])
    return d_default
    
def unstructure(d):
    """
    Flattens nested dictionary (if keys are used multiple places, they will be overwritten)
            
    :param d: (dict) dictionary to flatten
    :return: (dict) keys and values for each element in d
    """
    if isinstance(d, dict):
        d_new = {}
        for key in d:
            d_temp = unstructure(d[key])
            if isinstance(d_temp, None):
                d_temp[key] = d_temp.pop(None,d_temp[None])  
            d_new.update(d_temp)
        return d           
    else:
        return {None: d}
        
def structure(d_flat : dict, d_structure : dict, reject_nonexistent : bool = True):
    """
    Maps dictionary to a preferred structure 
    
    **This will consume d_flat**

    :param d_flat: (dict) dict containing values
    :param d_structure: (dict) dictionary containing structure and default values
    :param reject_nonexistent: (bool) If true, keys of d_flat not in d_structure will be thrown out, *default*: True
    :return: Structured dictionary
    """
    d_out = deepcopy(d_structure)
    for key in d_structure:
        if isinstance(d_structure[key], dict):
            d_out[key] = structure(d_flat, d_structure[key])
        elif key in d_flat:
            d_out[key] = deepcopy(d_flat[key])
            d_flat.pop(key)
            
    if not reject_nonexistent:
        d_out.update(d_flat)

    return deepcopy(d_out)

def find_key(d : dict, key):
    """
    Finds key in nested dict
    
    :param d: (dict) dictionary to search
    :param key: () key
    :return: (list) Returns order of keys to access element or None if nonexistent
    """
    if key not in dict:
        for k, val in d:
            if isinstance(val, dict):
                return [k] + find_key(val,key)
    else:
        return [key]
    return None
    
def recursive_set(d : dict, key, val):
    """
    Updates dictionary value given an ordered list of keys
    
    :param d: (dict) dictionary to update
    :param key: () key
    :param val: () value
    """
    if len(key) > 1:
        if key[0] not in d or isinstance(d[key[0]], dict):
            d[key[0]] = {}
        recursive_set(d[key[0]], key[1:len(key)], val)
    else:
        d[key[0]] = val