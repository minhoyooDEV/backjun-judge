import heapq
from collections import deque


def solution(jobs: list[int, int]):
    answer = 0
    startHeap = []
    for start, duration in jobs:
        heapq.heappush(startHeap, (start, duration))

    time = 0
    estimate_time = 0
    durationHeap = []
    lock = False
    time_checked = []

    while len(startHeap) or len(durationHeap) or time < estimate_time:
        while startHeap and (startHeap[0][0] <= time):
            task = heapq.heappop(startHeap)
            heapq.heappush(durationHeap, (task[1], task[0]))

        if lock == False:
            if (durationHeap and durationHeap[0][1] <= time):
                duration, start = heapq.heappop(durationHeap)
                estimate_time = duration + time
                time_checked.append(estimate_time - start)
                lock = True

        time += 1
        if estimate_time == time:
            lock = False
    for t in time_checked:
        answer += t

    return answer // len(jobs)


def solution2(jobs):
    print(jobs)
    tasks = deque(sorted([(x[1], x[0])
                          for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    print(tasks)
    heapq.heappush(q, tasks.popleft())
    print(tasks)
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        print('arr, dur', arr, dur)
        print('total_response_time', total_response_time)
        print('current_time', current_time)
        print('arr', arr)
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
            print(q)
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
            print(q)

    return total_response_time // len(jobs)


# print(solution([[1, 9], [0, 3], [2, 6]]), 9)
print(solution2([[1, 9], [0, 3], [2, 6]]), 9)
# print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
# print(solution2([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution2([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[100, 100], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)


# import heapq
