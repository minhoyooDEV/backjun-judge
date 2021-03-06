# dfs, bfs

from collections import deque


def dfs(v, g, checked):
    print(v, end=' ')
    checked[v] = True
    for e in g[v]:
        if not checked[e]:
            dfs(e, g, checked)


def bfs(v, g, c):
    q = deque([v])
    while q:
        v = q.popleft()
        if not c[v]:
            
            c[v] = True
            print(v, end= ' ')
            for e in g[v]:
                if not c[e]:
                    q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()


dfs(v, adj, [False for _ in range(n + 1)])
print()
bfs(v, adj, [False for _ in range(n + 1)])