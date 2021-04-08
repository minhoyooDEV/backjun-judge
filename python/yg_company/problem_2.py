from collections import defaultdict


def func(l: list[int]):

    # 누적값 저장
    m = defaultdict(int)
    zero_set = []
    exceed_set = []
    length = len(l)

    for n in l:
        m[n] += 1

    print(m)

    for n in range(1, length + 1):
        if m[n] == 0:
            zero_set.append(n)
        elif m[n] > 1:
            for _ in range(m[n] - 1):
                exceed_set.append(n)

    result = 0

    while zero_set:
        target_n = zero_set.pop()
        exceed_n = exceed_set.pop()

        result += abs(exceed_n - target_n)
    print(result)
    return result


func([1, 2, 1])
func([2, 1, 4, 4])
func([6, 2, 3, 5, 6, 3])
func([6, 2, 3, 5, 6, 6])
