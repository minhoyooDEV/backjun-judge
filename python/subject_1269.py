# dfs, bfs

from typing import DefaultDict

n, m, v = map(int, input().split())

graph = DefaultDict(list)

for _ in range(m):
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])


def bfs(start, g):
    checked = [False for _ in range(len(g) + 1)]
    checked[start] = True
    list = [start]
    queue = sorted([d for d in g[start]])

    while queue:
        target = queue.pop(0)
        if not checked[target]:
            queue = queue + sorted(g[target])
            checked[target] = True
            list.append(target)

    return list


def dfs(start, g):
    checked = [False for _ in range(len(g) + 1)]
    checked[start] = True
    list = [start]
    stack = sorted([d for d in g[start]])

    while stack:
        target = stack.pop(0)
        if not checked[target]:
            stack = sorted(g[target]) + stack
            checked[target] = True
            list.append(target)

    return list


print(' '.join(map(str, dfs(v, graph))))
print(' '.join(map(str, bfs(v, graph))))
