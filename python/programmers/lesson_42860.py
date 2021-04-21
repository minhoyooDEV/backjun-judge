from collections import deque

def solution(name):
    length = len(name)
    diffs = [float('inf')] * length
    answer = 0
    ordA = ord('A')
    ordZ = ord('Z')
    midDiff = (ordZ - ordA)//2
    # print(midDiff)
    names = list(name)

    for i, s in enumerate(names):
        diff = ord(s) - ordA

        ch = 'up'
        if diff >= midDiff:
            diff = ordZ - ord(s) + 1
            ch = 'down'

        print(diff, ch)
        diffs[i] = diff
        answer += diff

    # print(diffs)
    namesq = deque(names[length//2:] + names[:length//2])
    q_mid = length//2
    # while True:
    #     print(names)
    moveCount = 0
    while True:
        namesq[q_mid] = 'A'

        for i in range(1, q_mid + 1):
            if namesq[q_mid + i]:
                pass
            elif namesq[q_mid - i ]:
                pass


    print(namesq, q_mid)
    # print(names[:len(names) //2])
    # print(names[len(names) //2:])
    return answer

print(solution('JAEAAANW'))
# a b c d e f g h i j k l m
# n o p q r s t u v w x y z
# [0, 4, 0, 0, 0, 13, 9, 0, 4, 0, 0, 0, 13]
# [9, 0, 4, 0, 0,  0,13, 9, 0, 4, 0, 0, 0,]