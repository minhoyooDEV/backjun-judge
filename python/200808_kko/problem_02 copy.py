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

        for personPos in personPosSet:
            visited_road = copy.deepcopy(roadData)
            q = deque()

            if findFlag:
                result.append(0)
                break


            # pprint.pprint(visited)

            while q:

            def dfs(x, y):
                nonlocal findFlag

                for i in range(4):
                    nX = x + dX[i]
                    nY = y + dY[i]

                    if x > 4 or x < 0 or y > 4 or y < 0:
                        return
                    if not visited[nX][nY]:
                        return

                    if place[nX][nY] == 'P' and personPos[0] != x and personPos[1] != y:
                        xx, yy = personPos
                        # print(xx, yy)
                        diff = abs(x - xx) + abs(y-yy)  # 거리두기길이
                        print('diff', diff, diff < 3)
                        if diff < 3:
                            findFlag = True
                            # print(True)
                        return

                    # visited[nX][nY] = False

                    # print(nX, nY)
                    dfs(nX, nY)

            dfs(personPos[0], personPos[1])

        if not findFlag:
            result.append(1)

    # print(result)
    return result


print(solution([
    # ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    # ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
    # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]))
