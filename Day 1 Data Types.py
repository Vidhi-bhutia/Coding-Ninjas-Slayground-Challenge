from typing import *
import sys
def dataTypes(data):
    if data == 'Integer':
        size = sys.getsizeof(int())
    if data == 'Long':
        size = sys.getsizeof(long())
    if data == 'Float':
        size = sys.getsizeof(float())
    if data == 'Double':
        size = sys.getsizeof(float()) * 2
    if data == 'Character':
        size = sys.getsizeof(str())
    print(size)
d = input("Enter data type: ")
dataTypes(d)
