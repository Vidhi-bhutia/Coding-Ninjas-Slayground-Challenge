from os import *
from sys import *
from collections import *
from math import *


def printPattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
