# 힙큐, minimum_queue

import heapq

count = int(input())

min_q = []
for _ in range(count):
    n = int(input())

    if n == 0:
        if min_q:
            print(heapq.heappop(min_q))
        else:
            print(0)
    else:
        heapq.heappush(min_q, n)
