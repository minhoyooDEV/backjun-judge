def solution(A):

    n = len(A)

    dp = [[0 for x in range(2)] for y in range(n)]

    if A[n-1] == 0:

        dp[n-1][0] = 0

        dp[n-1][1] = 1

    else:

        dp[n-1][0] = 1

        dp[n-1][1] = 0

    for i in reversed(range(len(A)-1)):

        if A[0] == 0:

            dp[i][0] = dp[i+1][1]

            dp[i][1] = dp[i+1][0] + 1

        else:

            dp[i][0] = dp[i+1][1] + 1

            dp[i][1] = dp[i+1][0]

    print(dp[0][0], dp[0][1])
    return min(dp[0][0], dp[0][1])


solution([1, 0, 1, 0, 1, 1])
