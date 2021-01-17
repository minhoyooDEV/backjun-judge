# 탐색
n = int(input())
sec = 0
k = 0
while n != 0:
    if k + 1 <= n:
        k += 1
    else:
        k = 1
    n -= k
    sec += 1
print(sec)


# k = 1
# while n != 0:
#     if k < n:
#         k = 1
#     n -= k
#     k += 1
