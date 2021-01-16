# 재귀함수

n, r, c = map(int, input().split(' '))
count = 0

def func(x, y, size):
    global count
    # size제일 작을 때만 확인한다
    if size == 2:
        if x == r and y == c:
            print(count)
            return
        count += 1
        if x == r and y + 1 == c:
            print(count)
            return
        count += 1
        if x + 1 == r and y == c:
            print(count)
            return
        count += 1
        if x + 1 == r and y + 1 == c:
            print(count)
            return
        count += 1
        return

    func(x, y, size / 2)
    func(x, y + size / 2, size / 2)
    func(x + size / 2, y, size / 2)
    func(x + size / 2, y + size / 2, size / 2)


func(0, 0, 2 ** n)
