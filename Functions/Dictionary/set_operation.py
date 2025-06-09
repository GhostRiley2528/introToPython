set = {"orange", "yellow"}
set0 = {"red", "blue"}
print("Original sets:")
print("Set:", set)
print("Set0:", set0)
#intersection
set1 = set.intersection(set0)
print("Intersection of set and set0:", set1)
#union
set2 = set.union(set0)
print("Union of set and set0:", set2)
#difference
set3 = set.difference(set0)
print("Difference of set and set0:", set3)
#symmetric_difference
set4 = set.symmetric_difference(set0)
print("Symmetric difference of set and set0:", set4)
#issubset
print("Is set a subset of set0?", set.issubset(set0))
#issuperset
print("Is set a superset of set0?", set.issuperset(set0))
