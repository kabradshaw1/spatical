rows, cols = 2, 4
arr = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)


for n in range(0, 7+1):
    row = int(n/cols)
    col = n%cols
    print(row, col)
    arr[row][col] = n
print(arr)

