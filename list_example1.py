g1 = []
for i in range(10+1):
    g1.append(i*10)

print("Reference operator []: g1[2]", g1[2])

# Python iterator only has next method 
it = iter(g1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
