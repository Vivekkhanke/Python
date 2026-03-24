list =[1,2,2,4,4,5]
s= set(list)
print(s)
# ---------------------

s = {1,2,3}
# s.add(10)
# print(s)

s.update([4,5,6])
print(s)

# s.remove(8)
# print(s)

s.discard(5)
print(s)
# --------------------------------

# Union (combile)
a = {1,2,3}
b = {3,4,5}

print(a | b)

# Intersection
print(a & b)

# Difference
print(a-b)

s = {5,10,2,1,33}
print(55 in s)

# Looping through set
s = {5,10,2,1,33}

for i in s:
    print(i)
    
