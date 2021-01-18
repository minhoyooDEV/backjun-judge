# 탐색

n, m = map(int, input().split(' '))

data = [input() for _ in range(n)]

row = [0]*n
col = [0]*m

for x in range(n):
    for y in range(m):
        if data[x][y] == 'X':
            row[x] = 1
            col[y] = 1

row_count = 0
for x in range(n):
    if row[x] == 0:
        row_count +=1

col_count = 0
for y in range(m):
    if col[y] == 0:
        col_count +=1

print(max(row_count, col_count))