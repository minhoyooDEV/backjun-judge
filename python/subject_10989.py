# 계수정렬
import sys
size = 100001
case = int(sys.stdin.readline())

l = [0] * size

for _ in range(case):
    l[int(sys.stdin.readline()) ] += 1

for i in range(size):
    for _ in range(l[i]):
        print(i)
