from os import *
from sys import *
from collections import *
from math import *

def termsOfAP(x):
    series = []
    n = 1
    while len(series) < x:
        term = 3 * n + 2
        if term % 4 != 0:
            series.append(term) 
        n += 1
    return series
