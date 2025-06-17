seta = {2,8,16,24,32}
setb = {3,8,12,24}
#all funtcions like union, intersection, difference, symmetric difference also reverse the sets
# and return a new set, they do not modify the original sets.
print("Set A:", seta)
print("Set B:", setb)
print("Union of A and B:", seta.union(setb))
print("Intersection of A and B:", seta.intersection(setb))
print("Difference of A and B:", seta.difference(setb))
print("Symmetric difference of A and B:", seta.symmetric_difference(setb))
print("Is A a subset of B?", seta.issubset(setb))
print("Is A a superset of B?", seta.issuperset(setb))
print("Length of Set A:", len(seta))
print("Length of Set B:", len(setb))
print("Is Set A empty?", not seta)
print("Is Set B empty?", not setb)
print("Set A in ascending order:", sorted(seta))
print("Set B in ascending order:", sorted(setb))
print("Set A in descending order:", sorted(seta, reverse=True))
print("Set B in descending order:", sorted(setb, reverse=True))