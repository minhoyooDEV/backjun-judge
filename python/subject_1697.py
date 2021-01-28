# bfs

from collections import deque

MAX = 100001
n, k = map(int, input().split())

ary = [0] * MAX


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return ary[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, 2 * now_pos):
            if 0 <= next_pos < MAX and not ary[next_pos]:
                ary[next_pos] = ary[now_pos] + 1
                q.append(next_pos)


print(bfs())
