# 트리

case_size = int(input())

tree = {}

for _ in range(case_size):
    root, left, right = map(int, input().split())

    tree[root] = {'left': left if left != -1 else None,
                  'right': right if right != -1 else None}
level_data = {}
distance = {}
d_level = 0


def in_order(graph, root, level):
    global d_level
    if not root:
        pass
    else:
        in_order(graph, graph[root]['left'], level + 1)
        d_level += 1
        distance[root] = d_level

        if level in level_data:
            level_data[level].append(root)
        else:
            level_data[level] = [root]
        # print(root, level, d_level)
        in_order(graph, graph[root]['right'], level + 1)


in_order(tree, 1, 1)

max_distance_data = {l: distance[level_data[l][-1]] -
                     distance[level_data[l][0]] + 1 for l in level_data}

result = sorted(max_distance_data.items(), key=lambda x: x[1])[-1]
print(str(result[0]) + ' ' + str(result[1]))
