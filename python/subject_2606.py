# bfs

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
count = 0

def dfs(n):
    global count
    if not visited[n]:
        visited[n] = True
        if n != 1:
            count += 1
        for i in adj[n]:
            dfs(i)


dfs(1)

print(count)