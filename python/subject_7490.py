# 재귀함수

case = int(input())


def func(x, n, s, l):
    if x == n:
        if eval(s.replace(' ', '')) == 0:
            l.append(s)
        return

    next = x + 1

    func(next, n, s + '+' + str(next), l)
    func(next, n, s + '-' + str(next), l)
    func(next, n, s + ' ' + str(next), l)


for i in range(case):
    n = int(input())

    arr = []
    func(1, n, '1', arr)
    arr.sort()
    for s in arr:
        print(s)

    if i != case - 1:
        print()
