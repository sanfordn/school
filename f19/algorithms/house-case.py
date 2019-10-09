import sys
import random

cache = [None]*(1 + int(sys.argv[1]))
cache[0] = 0
cache[1] = 1

def get_house_values(houses):
    global cache
    if len(houses) == 0:
        return 0
    else:
        if not cache[len(houses) - 1]:
            get_house_values( houses[1:] )
        if not cache[len(houses) - 2]:
            get_house_values( houses[2:] )
        cache[len(houses)] = max( houses[0] + cache[len(houses) - 2], cache[len(houses) - 1])

houses = [random.randint(1, 1000) for x in range(1, int(sys.argv[1]))]
get_house_values( houses )
print(cache[len(houses)])
