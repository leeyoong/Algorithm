def solution(block):
    left = block[0]
    long_block = block.index(max(block))
    water = 0
    for i in range(1, long_block):
        if max(left, block[i]) == block[i]:
            left = block[i]
        else:
            water += left - block[i]
    right = block[-1]
    for i in range(len(block)-2, long_block, -1):
        if max(right, block[i]) == block[i]:
            right = block[i]
        else:
            water += right - block[i]
    return water


h,w = map(int,input().split())
block = list(map(int,input().split()))
print(solution(block))