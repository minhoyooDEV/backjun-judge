from collections import defaultdict


def solution(weights, head2head):
    length = len(weights)
    winCnt = defaultdict(int)

    heavyWeightWinCnt = defaultdict(int)
    weightsdict = {i: weight for i, weight in enumerate(weights)}

    print('weightsdict', weightsdict)
    weightsort = sorted(weightsdict.items(), key=lambda x: x[1], reverse=True)
    print('weightsort', weightsort)
    weightidx = [i[0] for i in weightsort]
    print('weightidx', weightidx)

    for idx, vs in enumerate(head2head):
        for i in range(length):
            if vs[i] == "W":  # 승률 계산
                winCnt[idx] += 1
                if weights[idx] < weights[i]:  # 자신보다 무거운사람 이긴 횟수
                    heavyWeightWinCnt[idx] += 1

    heavyWeightdict = {i: heavyWeightWinCnt[i] for i in weightidx}

    heavyWeightSort = sorted(heavyWeightdict.items(),
                             key=lambda x: x[1], reverse=True)
    # print('heavyWeightWinCnt', heavyWeightWinCnt)
    # print('weightidx', weightidx)
    # print('heavyWeightdict', heavyWeightdict)
    # print('heavyWeightSort', heavyWeightSort)

    heavyWeightidx = [i[0] for i in heavyWeightSort]
    # print('heavyWeightidx', heavyWeightidx)

    winCntdict = {i: winCnt[i] for i in heavyWeightidx}
    # print('winCntdict', winCntdict)

    winCntSort = sorted(winCntdict.items(), key=lambda x: x[1], reverse=True)
    # print('winCntSort', winCntSort)

    winCntidx = [i[0] for i in winCntSort]
    # print('winCntidx', winCntidx)

    return list(map(lambda x: x+1, winCntidx))


if __name__ == "__main__":
    # weights = [50, 82, 75, 120]
    # weights = [145, 92, 86]
    weights = [60, 70, 60]
    # head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
    # head2head = ["NLW", "WNL", "LWN"]
    head2head = ["NNN", "NNN", "NNN"]
    print(solution(weights, head2head))
