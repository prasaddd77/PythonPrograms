s = set()
print(type(s))
l = [2,3,586]
s1 = set(l)
print(s1)
print(type(s1))
s.add(1)
print(s)
s.add(2)
print(s.union({1,9}))
print(s)
print(s.isdisjoint(s1))
s1.remove(586)
print(s1)
s.intersection(s1)



