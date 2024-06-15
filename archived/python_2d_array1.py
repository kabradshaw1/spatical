rows, cols = 2, 4
arr = [[0]*cols]*rows
print(arr)
for n in range(0, 7+1):
    row = int(n/cols)
    col = n%cols
    print(row, col)
    arr[row][col] = n
print(arr)

