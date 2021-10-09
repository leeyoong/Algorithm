n = int(input())
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1
def fibo(k):
    if dp[k] != -1:
        return dp[k]
    dp[k] = fibo(k-1) + fibo(k-2)
    return dp[k]
fibo(n)
print(dp[-1])