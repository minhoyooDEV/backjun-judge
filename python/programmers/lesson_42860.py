from collections import deque


def solution(name):
    length = len(name)
    diffs = [0] * length
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

        # print(diff, ch)
        diffs[i] = diff
        answer += diff

    namesq = deque(names)
    print(namesq)
    print()
    q_mid = length//2
    for _ in range(q_mid):
        namesq.appendleft(namesq.pop())

    # print(namesq)
    # print()
    moveCount = 0
    while True:
        namesq[q_mid] = 'A'
        move = 0
        # print(namesq)
        for i in range(1, q_mid + 1):
            if namesq[q_mid - i] != 'A':
                for j in range(i):
                    namesq.appendleft(namesq.pop())
                move += i
                break
            if len(namesq) > (q_mid + i) and namesq[q_mid + i] != 'A':
                for j in range(i):
                    namesq.append(namesq.popleft())
                move += i
                break
        if not move:
            break

        moveCount += move
    print(sum(diffs), moveCount)
    return sum(diffs) + moveCount


print(solution('JEROEN'), 56)
print(solution('JAN'), 23)
print(solution('BBABA'), 6)
print(solution('BBBAAB'), 8)
print(solution('BBAABAA'), 7)
print(solution('BBAABBB'), 10)
print(solution('BBAABAAAA'), 7)
print(solution('BBAABAAAAB'), 10)
# a b c d e f g h i j k l m
# n o p q r s t u v w x y z
# [0, 4, 0, 0, 0, 13, 9, 0, 4, 0, 0, 0, 13]
# [9, 0, 4, 0, 0,  0,13, 9, 0, 4, 0, 0, 0,]
