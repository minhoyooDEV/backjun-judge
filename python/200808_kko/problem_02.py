from collections import deque
import copy


def solution(places: list[list[str]]):
    result = []
    dX = [-1, 1, 0, 0]
    dY = [0, 0, -1, 1]

    for place in places:

        personPosSet = set()
        roadData = [list(s) for s in place]

        findFlag = False

        # print(personPosSet)
        # if not personPosSet:
        #     result.append(0)
        #     continue

        for i in range(5):
            for j in range(5):
                if roadData[i][j] == 'P':
                    personPosSet.add((i, j))

        for personPos in personPosSet:

            if findFlag:
                result.append(0)
                break

            visited_road = copy.deepcopy(roadData)
            q = deque()
            q.append(personPos)
            visited_road[personPos[0]][personPos[1]] = 'X'
            # print('personPos', personPos[0])
            # print(visited_road)

            # pprint.pprint(visited)

            # print(q)
            while q:
                x, y = q.popleft()
                # print(x, y)
                for i in range(4):
                    nx, ny = x + dX[i], y + dY[i]

                    if nx > 4 or nx < 0 or ny > 4 or ny < 0:
                        continue
                    if visited_road[nx][ny] == 'X':
                        continue

                    if place[nx][ny] == 'P':
                        xx, yy = personPos
                        # print((xx, yy), (x, y))
                        diff = abs(nx - xx) + abs(ny - yy)  # 거리두기길이
                        # print('diff', diff, diff < 3)
                        if diff < 3:
                            findFlag = True
                            # print(True)
                        continue
                    visited_road[nx][ny] = 'X'
                    q.append((nx, ny))

        if not findFlag:
            result.append(1)

    # print(result)
    return result


print(solution([
    # ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    # ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
    # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]
]))
