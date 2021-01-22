import heapq

case = int(input())

heap = []
for _ in range(case):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a + b
    result += sum
    heapq.heappush(heap, sum)

print(result)
