n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [set() for _ in range(n)]

if s+v[0] <= m:
    dp[0].add(s+v[0])
if s-v[0] >= 0:
    dp[0].add(s-v[0])


def solution():
    if len(dp[0]) == 0:
        return -1
    for j in range(len(dp)-1):
        for d in list(dp[j]):
            if d+v[j+1] <= m:
                dp[j+1].add(d+v[j+1])
            if d - v[j+1] >= 0:
                dp[j + 1].add(d - v[j+1])
        if len(dp[j+1]) == 0:
            return -1
    return max(dp[-1])


print(solution())