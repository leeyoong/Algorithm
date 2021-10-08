n = int(input())
dp = [[0] * n for _ in range(n)]
g = []
cnt = 0
for _ in range(n):
    g.append(list(map(int, input().split())))

dp[0][0] = 1

for y in range(n):
    for x in range(n):
        d = g[y][x]
        dx = [0,d]
        dy = [d,0]

        if not dp[y][x] or (y == n-1 and x == n-1):
            continue

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                dp[ny][nx] += dp[y][x]
print(dp[n-1][n-1])