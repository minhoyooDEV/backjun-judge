# 4 7

# 3 4
# 2 3
# 2 1

# 2 3
# 3 1
# 3 1
# 3 3
# 2 4
# 3 4
# 2 4


class Node:
    def __init__(self, name):
        self.name = name
        self.data = []


N, Q = map(int, input().split())
# N: 테스트될 사람 2이상 100이하
# M: N명간의 친구 관계의 수 5천이하

# print(N, M)

g = {}
friends = input().split()
# friends = "A B C D E P Q".split()
for name in friends:
    # g[name] = Node(name)
    g[name] = Node(name)

# print(g)
for _ in range(M):
    s = input().split()
    a, b = s
    g[a].data.append(b)
    g[b].data.append(a)


for name in g:
    node = g[name]

    visited = set([name])
    queue = [name]

    while queue:
        target_name = queue.pop()
        target = g[target_name]
        for friend_name in target.data:
            if not friend_name in visited:
                visited.add(friend_name)
                queue.append(friend_name)

for nm in g:
    node = g[nm]

mx_count = 0
result = ''

for nm in g:
    node = g[nm]

    for nm2 in g:
        if nm == nm2:
            continue

        node2 = g[nm2]

        if nm in node2.data:
            continue

        res = set(node.data).intersection(set(node2.data))
        if len(res) > mx_count:
            mx_count = len(res)
            temp = sorted([nm, nm2])
            result = temp[0] + ' ' + temp[1]


print(result)
print(mx_count)


# print(node.friends)
# 7 8
# A B C D E P Q
# P A
# P B
# P C
# P D
# Q B
# Q C
# Q D
# Q E
