import math
import time 

start = time.time()
N = 100000
dx = math.pi/N
area = 0
for i in range(0, N):
    x = dx * i
    y = math.sin(x)
    area += y * dx
end = time.time()
print("area = %s "%area)
print("execution time: %f seconds"%(end-start))


