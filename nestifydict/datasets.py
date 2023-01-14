"""
Nestify dict adding for dealing with unstructured datasets
"""
__license__ = "BSD-3"
__docformat__ = 'reStructuredText'
__author__ = "Jared Beard"

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

__all__ = ["expand_generator", "expand_list", "expand_file", "compress", "compress_file"]

def compress(data : list):
    """
    Compresses data structured as a list of flat dictionaries
    
    :return: (dict) compressed data
    """
    
    # Check for unique point structures
    
    # for each set of subset of data
    # Get the number of unique values for each dimension.
    # Take the point with the fewest unique values and make those the keys
    # if it is a list or set then store as a list