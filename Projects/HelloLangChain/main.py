from math import sqrt


listA = [1, 2, 3]
mapList = (item*2 for item in listA)
newmap = map(lambda *a: a, range(3), ('a', 'b', 'c'), [9, 9, 9])



