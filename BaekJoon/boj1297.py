start, end = map(int, input().split())
sequence = []
cnt = 1
while len(sequence) < end:
    sequence += [cnt] * cnt
    cnt += 1
print(sum(sequence[start-1:end]))