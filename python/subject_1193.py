n = int(input())

if n == 1:
    print("1/1")

sum = 1
cnt = 0
num = 1

while True:
    sum += 1
    cnt += num
    if cnt >= n:
        break
    num += 1

child, parent = 1, 1
if sum % 2:
    child = sum - 1
else:
    child = sum - 1

while True:
    if cnt == n:
        break
    if sum % 2:
        parent += 1
        child -= 1
    else:
        parent -= 1
        child += 1

    cnt -= 1

print(str(parent) + "/" + str(child))
