import time

#starting time
start = time.time()

for i in range(30):
    print(i)

#end time 
end = time.time()

#total time taken
print("Execution time %s seconds"%(end-start))

