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

    sums = [i for i in range(1, n+1)]

    for _ in range(k):
        for j in range(1, n):
            sums[j] += sums[j -1]
    print(sums[-1])


