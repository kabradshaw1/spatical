g1 = []
for i in range(10+1):
    if i%4==0:
        g1.append(i*10)
    elif i%4==1:
        g1.append(i*10.0)
    elif i%4==2:
        g1.append(str(i*10))
    else:
        g1.append([i*10])

print(g1) 
