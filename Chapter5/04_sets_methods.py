s={1,5,32,54,5,5,5,"harry"}
print(s,type(s))
s.add(566)
print(s,type(s))

s.update([3,4])
print(s,type(s))

s.remove(3)
print(s,type(s))

s.discard(4)
print(s,type(s))

s.pop() #remove random element
print(s,type(s))

s.clear()
print(s,type(s))

a={1,2}
b={2,3}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

a={1,2}
b={1,2,3}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))