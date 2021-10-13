from collections import deque

n = int(input())
net = int(input())
edges = []
for _ in range(net):
    edges.append(list(map(int,input().split())))

virus = []
virus_deque = deque()
virus_deque.append(1)

while len(virus_deque) != 0:
    v = virus_deque.pop()
    virus.append(v)
    for edge in edges:
        if v in edge:
            if edge[0] not in virus and edge[0] not in virus_deque:
                virus_deque.append(edge[0])
            elif edge[1] not in virus and edge[1] not in virus_deque:
                virus_deque.append(edge[1])
print(len(virus) - 1)
