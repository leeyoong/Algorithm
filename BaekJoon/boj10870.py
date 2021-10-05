def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    pibo = [0,1]
    for i in range(2, n+1):
        pibo.append(pibo[i - 1] + pibo[i - 2])
    return pibo[-1]


print(solution(int(input())))