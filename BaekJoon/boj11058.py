n = int(input())
dp = [0] * (n+1)
if n <= 6:
    print(n)
else:
    for i in range(6):
        dp[i+1] = i+1
    for i in range(7, n+1):
        for j in range(3, n+1):
            if i-j < 0:
                break
            dp[i] = max((j-1) * dp[i-j], dp[i])
    print(dp[-1])
