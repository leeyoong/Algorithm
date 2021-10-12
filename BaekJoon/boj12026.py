from collections import defaultdict
import sys
inf = sys.maxsize
n = int(input())
routes = input()
route_dict = defaultdict(list)
dp = [inf] * n
for i,route in enumerate(routes):
    route_dict[route].append(i)
dp[0] = 0

def update_dp(position, new):
    for j in route_dict[new]:
        if j > position:
            dp[j] = min(dp[j], dp[position] + (j - position) ** 2)


for i in range(len(routes)):
    if routes[i] == 'B':
        update_dp(i, 'O')
    elif routes[i] == 'O':
        update_dp(i, 'J')
    else:
        update_dp(i, 'B')
if dp[-1] == inf:
    print('-1')
else:
    print(dp[-1])