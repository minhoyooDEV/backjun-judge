# 트리

case_size = int(input())

tree = {}

for _ in range(case_size):
    root, left, right = input().split()

    tree[root] = {'left': None, 'right': None}
    
    if left != '.':
        tree[root]['left'] = left
    if right != '.':
        tree[root]['right'] = right


def pre_order(root, graph):
    if root is None:
        pass
    else:
        print(root, end='')
        pre_order(graph[root]['left'], graph)
        pre_order(graph[root]['right'], graph)

def in_order(root, graph):
    if root is None:
        pass
    else:
        in_order(graph[root]['left'], graph)
        print(root, end='')
        in_order(graph[root]['right'], graph)

def post_order(root, graph):
    if root is None:
        pass
    else:
        post_order(graph[root]['left'], graph)
        post_order(graph[root]['right'], graph)
        print(root, end='')


pre_order('A', tree)
print()
in_order('A', tree)
print()
post_order('A', tree)
