m = int(input())
n = int(input())
sol = []
for x in range(m,n+1):
    if x == 1:
        continue
    elif x % 2 == 0:
        if x == 2:
            sol.append(x)
        continue
    skip = False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            skip = True
            break
    if skip is False:
        sol.append(x)
if len(sol) == 0:
    print(-1)
else:
    print("{}\n{}".format(sum(sol), sol[0]))