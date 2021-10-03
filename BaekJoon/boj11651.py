n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().split()))
arr.sort(key=lambda x:(x[1], x[0]))
print(arr)
for i in range(n):
    print("{} {}".format(arr[i][0], arr[i][1]))