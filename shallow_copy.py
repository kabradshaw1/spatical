import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
print("\n")

li2[0] = 10
li2[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")

print ("The elements of li2")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
