case = int(input())

l = []

for _ in range(case):
    data = list(map(int, input().split(' ')))
    l.append((data[0], data[1]))

l.sort(key=lambda x: x[1])
l.sort(key=lambda x: x[0])

for d in l:
    print(d[0],d[1])
