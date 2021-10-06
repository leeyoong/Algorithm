t = int(input())
for i in range(t):
    prob = list(map(int, input().split()))
    prob.sort(reverse=True)
    print(prob[2])