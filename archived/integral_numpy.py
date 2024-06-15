import numpy as np
import time 

start = time.time()
N = 100000
dx = np.pi/N
x = np.linspace(0, np.pi, N)
y = np.sin(x)
area =(y*dx).sum()

end = time.time()
print("area = %s "%area)
print("execution time: %f seconds"%(end-start))


