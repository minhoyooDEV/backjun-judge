def solution(brown: int, yellow: int):
    answer = []
    total = brown + yellow

    for i in range(1, total // 2 + 1):
        x = i
        y = total // i

        if x >= y:
            if x * y == total:
                if (x - 2) * (y -2) == yellow:
                    answer.append(x)
                    answer.append(y)
                    break

    return answer


print(solution(10, 2))
# print(solution(8, 1))
# print(solution(24, 24))
