#union find

case = int(input())

def find(node):
    if parent[node] != node:
        p = find(parent[node])
        parent[node] = p
        return parent[node]
    else:
        return node

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        size_pool[x] += size_pool[y]

for _ in range(case):
    f = int(input())
    parent = {}
    size_pool = {}

    for _ in range(f):
        a, b = input().split(' ')

        if a not in parent:
            parent[a] = a
            size_pool[a] = 1

        if b not in parent:
            parent[b] = b
            size_pool[b] = 1

        union(a, b)
        print(size_pool[find(a)])
