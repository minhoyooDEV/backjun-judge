import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    if heap[0] >= K:
        return 0

    while len(heap) > 1:
        answer += 1
        v1 = heapq.heappop(heap)
        v2 = heapq.heappop(heap)
        result = v1 + v2 * 2
        heapq.heappush(heap, result)

        if result >= K:
            return answer

    answer = -1

    return answer


print(solution([1, 1, 1], 4) == 2)
print(solution([10, 10, 10, 10, 10], 100) == 4)
print(solution([1, 2, 3, 9, 10, 12], 7) == 2)
print(solution([0, 2, 3, 9, 10, 12], 7) == 2)
print(solution([0, 0, 3, 9, 10, 12], 7) == 3)
print(solution([0, 0, 0, 0], 7) == -1)
print(solution([0, 0, 3, 9, 10, 12], 7000) == -1)
print(solution([0, 0, 3, 9, 10, 12], 0) == 0)
print(solution([0, 0, 3, 9, 10, 12], 1) == 2)
print(solution([0, 0], 0) == 0)
print(solution([0, 0], 1) == -1)
print(solution([1, 0], 1) == 1)
