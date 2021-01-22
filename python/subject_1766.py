# 위상정렬 O(V+E), 힙

import heapq

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

heap = []

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    indegree[y] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)

    for y in arr[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')
