from functools import reduce

def solution(n: int, lost: list[int], reserve: list[int]):
    answer = 0
    data = [0] * (n + 1)

    for i in range(1, n + 1):
        data[i] += 1

    for i in lost:
        data[i] -= 1

    for i in reserve:
        data[i] += 1

    for i in range(1, n):
        if i != 1 and data[i - 1] == 0 and data[i] == 2:
            data[i - 1] += 1
            data[i] -= 1

        if i != n and data[i - 1] == 2 and data[i] == 0:
            data[i - 1] -= 1
            data[i] += 1

    for num in data:
        if num >= 1:
            answer += 1

    # print(data)
    # result = reduce(lambda acc, cur: acc + (cur if cur >= 1 else 0), data, 0 )
    # print(result)

    return answer


print(solution(5, [2, 4], [1, 3, 5]), 5)
print(solution(5, [2, 4], [3]), 4)
print(solution(3, [3], [1]), 2)
