class Node:
    win = None
    loss = None

    def __init__(self):
        self.win = []
        self.loss = []


def solution(n, results):
    answer = 0
    g = {}
    for i in range(1, n + 1):
        g[i] = Node()

    for a, b in results:
        g[a].win.append(b)
        g[b].loss.append(a)

    for i in range(1, n + 1):
        q = []
        visited = {i}
        q.append(g[i])


        while q:
            node = q[0]
            del q[0]
            for new_node in node.loss:
                if new_node not in visited:
                    visited.add(new_node)
                    q.append(g[new_node])

            for new_node in node.win:
                if new_node not in visited:
                    visited.add(new_node)
                    q.append(g[new_node])

        if len(visited) == n:
            answer += 1

    print(answer)

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
