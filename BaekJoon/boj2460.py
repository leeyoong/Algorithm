def solution(prob_list):
    answer = []
    n = 0
    for i in range(len(prob_list)):
        n = n - prob_list[i][0] + prob_list[i][1]
        answer.append(n)
    return max(answer)


prob_list = []
for i in range(10):
    prob_list.append(list(map(int, input().split())))
print(solution(prob_list))