import itertools
def solution(prob):
    res = list(itertools.combinations(prob,7))
    for re in res:
        if sum(re) == 100:
            answer = ''
            ans = sorted(re)
            for i in range(7):
                answer += str(ans[i]) + '\n'
            return answer[:-1]
prob = []
for i in range(9):
    prob.append(int(input()))
print(solution(prob))