"""Gnome sort (nicknamed stupid sort) is a variation of the insertion sort sorting algorithm that does not use nested loops. """
def gnome_sort(collection):
    i = 0
    while i < len(collection):
        if collection[i-1] <= collection[i]:
            i += 1
        else:
            collection[i-1], collection[i]  = collection[i], collection[i-1]
            i -= 1
            if i == 0:
                i = 1
        print(collection)
    return collection

if __name__ =="__main__":
    try:
        collection = [int(item) for item in input().split()]
    except:
        print("Not an Int")
    # 5 0 4 3 2 1
    sorted = gnome_sort(collection)
