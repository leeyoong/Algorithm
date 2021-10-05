def solution(n):
    str_bit = ''
    while n>1:
        n,r = divmod(n,2)
        str_bit += str(r)
    str_bit += str(n)
    answer = ''
    for i in range(len(str_bit)):
        if str_bit[i] == '1':
            answer += str(i)+' '
    return answer


case = int(input())
for i in range(case):
    print(solution(int(input())))