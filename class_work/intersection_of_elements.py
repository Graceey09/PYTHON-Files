def intersection(element1, element2):
    intersect = []
    for items in element1:
        for item in element2:
            if item == items and item not in intersect:
                intersect += [item]
    return tuple(intersect)


element1 = [10, 20, 70, 40, 30, 40, 50, 60, 60, 60]
element2 = [70, 70, 70, 80, 90, 10, 35, 60, 40, 10, 65]
print(intersection(element1, element2))
