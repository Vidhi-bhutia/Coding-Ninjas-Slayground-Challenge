from os import * 
from sys import * 
from collections import * 
from math import *

def checkDiff(arr, N, K):    # Write your code here.    
    diff_set = set()   
    for num in arr:
        if num - K in diff_set or num + K in diff_set:
            return True
        diff_set.add(num)

    return False 
