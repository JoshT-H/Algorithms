""" Binary search, also known as half-interval search,[1]
logarithmic search,[2] or binary chop,[3] is a search algorithm
 that finds the position of a target value within a sorted array."""

import math


def iterative_binary_search(collection, target):
    collection.sort()

    high = collection.index(max(collection))
    low = collection.index(min(collection))
    while low!=high:
        mid = math.ceil((low + high)/2)
        if target == collection[mid]:
            return mid
        elif target > collection[mid]:# target is on the righthand side
            low = mid + 1
        else: # target is on the lefthand side
            high= mid - 1


if __name__ == "__main__":
    try:
        target =int(input().split())
        collection = [int(item) for item in input().split()]
    except:
        print("Not an Int")
    # 5
    # 5 0 4 3 2 1
    sorted = iterative_binary_search(collection, target)
    
    


