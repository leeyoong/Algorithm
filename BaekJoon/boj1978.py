n = int(input())
prob = list(map(int, input().split()))
answer = 0
for i in range(n):
    if prob[i] == 1:
        continue
    elif prob[i] % 2 == 0:
        if prob[i] == 2:
            answer += 1
        continue
    status = False
    for j in range(3,int(prob[i]**0.5)+1,2):
        if prob[i] % j == 0:
            status = True
            break
    if status == False:
        answer += 1
print(answer)