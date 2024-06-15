import matplotlib.image as mpimg
import numpy as np
import time

"""
Read the image.  This rquires the farm.tiff file to be in the same 
directory as this script.
"""
img = mpimg.imread("farm.tiff")

# Extract the red, green, and blue bands
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

# Print the data type and shapes of the three bands
print("Data type of bands:", r.dtype)
print("Shape of red band:", r.shape)
print("Shape of green band:", g.shape)
print("Shape of blue band:", b.shape)

# Find the median value of the green band using loops
start_time_loop = time.time()
green_1d = g.reshape(-1)
green_sorted = sorted(green_1d)
n = len(green_sorted)
if n % 2 == 0:
    median_loop = (green_sorted[n//2 - 1] + green_sorted[n//2]) / 2
else:
    median_loop = green_sorted[n//2]
end_time_loop = time.time()

# Find the median value of the green band using NumPy functions
start_time_numpy = time.time()
median_numpy = np.median(g)
end_time_numpy = time.time()

"""
Print the median values and time usage for both methods.
This demonstrates how much faster the NumPy method is.
Both are pretty fast with such a small task, but it could be
much more noticeable with larger tasks.
"""
print("Median value using loops:", median_loop)
print("Time usage for loop method:", end_time_loop - start_time_loop, "seconds")
print("Median value using NumPy:", median_numpy)
print("Time usage for NumPy method:", end_time_numpy - start_time_numpy, "seconds")
