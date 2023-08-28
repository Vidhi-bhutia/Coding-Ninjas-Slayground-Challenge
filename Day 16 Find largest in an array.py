from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    m = 0
    for i in arr:
        if i > m:
            m = i

    return m
