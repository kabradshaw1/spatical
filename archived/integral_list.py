import math
import time 

start = time.time()
N = 100000
dx = math.pi/N

da = [dx * math.sin(i*dx) for i in range(N)]
area = sum(da)

end = time.time()
print("area = %s "%area)
print("execution time: %f seconds"%(end-start))


