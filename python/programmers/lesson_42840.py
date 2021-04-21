def solution(answers):
    result = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    p = dict()
    p[1] = 0
    p[2] = 0
    p[3] = 0

    for i, answer in enumerate(answers):
        if answer == p1[i % len(p1)]:
            p[1] += 1
        if answer == p2[i % len(p2)]:
            p[2] += 1
        if answer == p3[i % len(p3)]:
            p[3] += 1
    mx = 0
    for k in p:
        mx = max(mx, p[k])
    for k in p:
        if mx == p[k]:
            result.append(k)
    result.sort()

    return result


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
