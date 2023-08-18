from os import *
from sys import *
from collections import *
from math import *
n = int(input())
temp = n
count = 0
while temp != 0:
    temp //= 10
    count += 1

temp = n
s = 0
while temp != 0:
    rem = temp % 10
    s += rem ** count
    temp //= 10

if s == n:
    print("true")
else:
    print("false")
