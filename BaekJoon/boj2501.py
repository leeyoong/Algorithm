def solution(n,k):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
            if cnt == k:
                return i
    return 0

n, k = map(int,input().split())
print(solution(n,k))