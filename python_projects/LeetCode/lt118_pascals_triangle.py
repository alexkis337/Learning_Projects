numRows = 7
result = [[1], [1, 1]]
for i in range(2, numRows):
    row = [1]
    for j in range(1, len(result[i-1])): row.append(result[i-1][j] + result[i-1][j-1])
    row.append(1)
    result.append(row)

print(result[6])

