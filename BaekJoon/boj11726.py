n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n == 1:
    print(1)
else:
    dp[2] = 2
    for i in range(3, len(dp)):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    print(dp[n])