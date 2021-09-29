def solution(weights, head2head):
    answer = []
    player = {i:[0,0,0,weights[i],0] for i in range(len(weights))}
    for i in range(len(weights)):
        for j in range(len(head2head)):
            if i == j:
                continue
            if head2head[i][j] != 'N':
                player[i][0] += 1
                if head2head[i][j] == 'W':
                    player[i][1] += 1
                    if weights[i] < weights[j]:
                        player[i][2] += 1
        if player[i][0] == 0:
            continue
        player[i][-1] = player[i][1] / player[i][0]
    res = sorted(player.items(), key = lambda x:(x[1][-1],x[1][-3],x[1][-2], -x[0]), reverse=True)
    answer = [out[0]+1 for out in res]
    return answer


print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86]	, ["NLW","WNL","LWN"]))
print(solution([60,70,60], ["NNN","NNN","NNN"]))
