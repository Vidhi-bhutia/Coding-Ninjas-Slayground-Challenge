from typing import *  

def countFrequency(n: int, m: int, arr: List[List[int]]):

    frequency = {}  # Dictionary to store frequency of elements

 

    # Count the frequency of each element

    for element in arr:

        if element in frequency:

            frequency[element] += 1

        else:

            frequency[element] = 1

 

    # Print only the frequencies in a single line

    # Create a list of frequencies

    frequencies = [frequency.get(num, 0) for num in range(1, n+1)]

    return frequencies
