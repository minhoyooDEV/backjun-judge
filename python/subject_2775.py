def getNum(k, n):
    if k == 0:
        return n
    if n == 1:
        return n

    return (getNum(k, n-1) + getNum(k - 1, n))


caseCount = int(input())
arr = list()
for _ in range(caseCount):
    k,n = 0,0
    while not(k > 0):
        print('k를 입력')
        k = int(input())
    while not(n > 0 and n <= 14):
        print('n을 입력')
        n = int(input())
    arr.append([k,n])

for index in range(len(arr)):
    [k, n] = arr[index]
    print(getNum(k,n))


