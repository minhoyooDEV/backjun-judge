

class Node:
    parent = None
    data = set()
    children = set()
    water = False

    def __init__(self, name):
        self.name = name


N, Q = map(int, '4 7'.split())
g = {}

for n in range(1, N + 1):
    g[n] = Node(n)

for a, b in [[3, 4], [2, 3], [2, 1]]:
    g[a].data.add(g[a])
    g[b].data.add(g[b])

visited = set([1])
queue = [g[1]]
print('aaa', queue)
while queue:
    target = queue.pop()
    print('----', queue)
    children = set(target.data)

    if target.parent:
        children.remove(target.parent)

    target.children = children

    print(target.name, len(target.children))
    for child in target.data:
        child_name = child.name
        # print(target.name, child_name)
        if not child_name in visited:
            g[child_name].parent = target
            visited.add(child_name)
            # print(visited)

            # print(target.name, child_name)
            queue.append(g[child_name])

    print('queue', queue)
    # if g[name].parent:
    #     print(g[name].parent.name)


# for q_type, target in [[2, 3], [3, 1], [3, 1], [3, 3], [2, 4], [3, 4], [2, 4]]:
#     pass
