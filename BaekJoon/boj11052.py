n = int(input())
p = [0]
p += list(map(int,input().split()))
for i in range(1, n+1):
    candi = []
    for j in range(i):
        candi.append(p[j] + p[i-j])
    p[i] = max(candi)

print(p[n])
