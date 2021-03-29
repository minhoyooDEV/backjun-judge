import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global count

    visited_x = [x]
    visited_y = [y]
    count += 1
    min([1,2], key=lambda x: x)
    while data:
        # print(data)
        found = False
        x, y = data.pop(0)
        if x in visited_x:
            for v_y in visited_y:
                if abs(v_y - y) == 1:
                    visited_y.append(y)
                    found = True
                    break

        elif y in visited_y:
            for v_x in visited_x:
                if abs(v_x - x) == 1:
                    visited_x.append(x)
                    found = True
                    break

        if not found:
            dfs(x, y)
            break


case = int(input())
for _ in range(case):
    m, n, k = map(int, input().split())

    count = 0
    data = []
    for _ in range(k):
        x, y = map(int, input().split())
        data.append((x, y))

    x, y = data.pop(0)
    # while data:
    dfs(x, y)

    print(count)
