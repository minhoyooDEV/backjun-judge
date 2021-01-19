# 이분탐색

k, n = map(int, input().split())

l = []
for _ in range(k):
    l.append(int(input()))

mn = 1
mx = max(l)
while mn <= mx:
    mid = (mn + mx) // 2
    acc = 0
    for i in l:
        acc += (i // mid)

    if acc >= n:
        mn = mid + 1
    else:
        mx = mid - 1

print(mx)