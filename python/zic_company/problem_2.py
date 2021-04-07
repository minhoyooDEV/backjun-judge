n = int(input())
l = list(map(int, input().split()))
length = len(l)
mx = 0


def dfs(result: int, cnt: int, visited: set):
    global mx

    for n in l:
        if n in visited:
            continue

        if cnt == length:
            result = result + (n * cnt)
            if (cnt % 2) == 0:
                result *= -1

            mx = max(mx, result)

        else:
            new_visited = set(visited)
            new_visited.add(n)

            value = n * cnt
            if (cnt % 2) == 0:
                value *= -1

            new_result = value + result

            dfs(new_result, cnt + 1, new_visited)


dfs(0, 1, set())

print(mx)
