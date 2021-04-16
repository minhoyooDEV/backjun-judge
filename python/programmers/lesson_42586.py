from collections import deque
import math
# def solution(progresses, speeds):
#     answer = []
#     q = deque(progresses)

#     while q:
#       for i in range(len(q)):
#         q[i] += speeds[i]

#       count = 0
#       while q and q[0] >= 100:
#         q.popleft()
#         count +=1

#       print(count, q)
#       if count:
#         answer.append(count)


def solution2(progresses, speeds):
    answer = []
    remain_progresses = deque([])
    for i, prog in enumerate( progresses):
      remain_progresses.append(math.ceil(100 - prog / speeds[i]))

    count = 0
    start_day = remain_progresses[0]
    for i, day in enumerate(remain_progresses):
      if day <= start_day:
          count += 1
      else:
        answer.append(count)
        start_day = day
        count = 1
    answer.append(count)

    return answer

# print(solution2( [0], [1]	), [1])
# print(solution2( [99, 99, 99] ,[1, 1,1]	), [3])
# print(solution2( [0, 1], [1, 100]	), [2])
# print(solution2( [2, 2, 1, 2], [1, 1, 1, 1]	), [])
# print(solution2([93, 30, 55]	,[1, 30, 5]	), [2,1])
# print(solution2([95, 90, 99, 99, 80, 99]		,[1, 1, 1, 1, 1, 1]		), [1,3,2])

def solution3(progresses, speeds):
    answer = []

    count = 0
    mx = 0
    for i, prog in enumerate( progresses):
      w = math.ceil(100 - prog / speeds[i])

      if count > 0 and mx < w:
        pass
      else:
        pass

      if mx < w:
        mx = w

      count += 1

    answer.append(count)

    return answer
