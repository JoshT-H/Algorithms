"""
Bubble sort (sinking sort), is a simple sorting algorithm that repeatedly steps through the input list element by element,
comparing the current element with the one after it,
swapping their values if needed
"""

def bubble(collection):
    flag  = sorted(collection)
    while collection != flag:
        for i in range(len(collection)-1):
            if collection[i] > collection[i+1]:
                collection[i], collection [i+1] = collection[i+1], collection[i]
            print(collection)
        if collection == flag: # If sort is
            break
    return collection


if __name__ == "__main__":
    try:
        # Example Input: 0, 5, 4, 3, 2, 1  ---> [0, 1, 2, 3, 4, 5]
        collection = [int(item) for item in input().split()]
    except:
        print("Sorry, not an int")
    sorted = bubble(collection)


