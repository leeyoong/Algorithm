k = int(input())
arr = []
answer = 0
for i in range(k):
    n = int(input())
    if n != 0:
        arr.append(n)
        answer += n
    else:
        answer -= arr.pop()
print(answer)