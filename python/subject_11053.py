n = int(input())

dp = [1] * n

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
