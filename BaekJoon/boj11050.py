n, k = map(int,input().split())
answer = n
divide = k
for i in range(1, k):
    answer *= n-i
    divide *= k-i
if k == 0:
    print(1)
else:
    print(int(answer/divide))