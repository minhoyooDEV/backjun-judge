# lcs

a = input()
b = input()

len_dp_a = len(a) + 1
len_dp_b = len(b) + 1

# dp1 = [[0] * len_dp_a] * len_dp_b #array question
dp = [[0] * len_dp_b for _ in range(len_dp_a)]

for i in range(1, len_dp_a):
    for j in range(1, len_dp_b):

        if a[i - 1] == b[j -1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(a)][len(b)])
