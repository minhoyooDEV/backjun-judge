# BFS, 이분탐색


from collections import deque


def bfs(m, s, e, ad):
    q = deque([s])
    visited = [False] * (n + 1)
    visited[s] = True

    while q:
        x = q.popleft()
        for y, w in ad[x]:
            if not visited[y] and w >= m:
                visited[y] = True
                q.append(y)
    return visited[e]


n, m = map(int, input().split(' '))
start = 1000_000_000
end = 1

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    adj[a].append((b, c))
    adj[b].append((a, c))
    start = min(start, c)
    end = max(end, c)

start_node, end_node = map(int, input().split(' '))

result = start

while start <= end:
    mid = (start + end) // 2
    if bfs(mid, start_node, end_node, adj):
        result = mid
        start = mid + 1
        pass
    else:
        end = mid - 1


print(result)
