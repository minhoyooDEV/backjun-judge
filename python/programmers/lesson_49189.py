from collections import defaultdict
from collections import deque


def solution(n, edge):
    answer = 0
    g = defaultdict(list)

    for a, b in edge:
        g[a].append(b)
        g[b].append(a)

    distances = [0] * (n + 1)
    distances[1] = 0

    visited = {1}
    q = deque([1])
    while q:
        x = q.popleft()

        print(q)
        for y in g[x]:
            if y not in visited:
                distances[y] = distances[x] + 1
                visited.add(y)
                q.append(y)

    mx = max(distances)

    for n in distances:
        if n == mx:
            answer += 1

    return answer


def solution2(n, edge):
    answer = 0

    # make-Graph
    G = dict()
    for e in edge:
        if e[0] in G:
            G[e[0]].append(e[1])
        else:
            G[e[0]] = [e[1]]
        if e[1] in G:
            G[e[1]].append(e[0])
        else:
            G[e[1]] = [e[0]]

    dist = [100000] * (n + 1)
    dist[1] = 0
    max_dist = 0

    # BFS
    visit = set()
    visit.add(1)
    q = [1]  # [vertex, dist]
    while q:
        x = q[0]
        del q[0]
        print(q)
        for y in G[x]:
            if y not in visit:
                dist[y] = dist[x] + 1
                max_dist = max(max_dist, dist[y])
                visit.add(y)
                q.append(y)
    print(max_dist)
    for x in range(2, n + 1):
        if dist[x] == max_dist:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution2(6, [[3, 6], [4, 3], [3, 2],
                    [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
# print(solution2(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [
#       3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
# print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
# print(solution(2, [[1, 2]]), 1)
# print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
# print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
# print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
# print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
# print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)
