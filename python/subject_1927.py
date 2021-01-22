# 힙큐, minimum_queue

import heapq

count = int(input())

min_q = []
result = []
for _ in range(count):
    n = int(input())

    if n == 0:
        if min_q:
            result.append(heapq.heappop(min_q))
        else:
            result.append(0)
    else:
        heapq.heappush(min_q, n)

for d in result:
    print(d)