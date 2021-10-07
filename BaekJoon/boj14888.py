import itertools


def solution(prob, cal):
    operation = ['+'] * cal[0] + ['-'] * cal[1] + ['*'] * cal[2] + ['//'] * cal[3]
    operations = set(itertools.permutations(operation, sum(cal)))
    out = []
    for oper in operations:
        out_str = prob[0]
        for i in range(len(oper)):
            if oper[i] == '//' and out_str[0] == '-':
                out_str = 'abs('+out_str+')'+oper[i]+prob[i+1]
                out_str = str(-eval(out_str))
            else:
                out_str += oper[i] + prob[i+1]
                out_str = str(eval(out_str))

        out.append(int(out_str))
    answer = str(max(out))+'\n'+ str(min(out))
    return answer


n = int(input())
prob = input().split()
cal = list(map(int, input().split()))
print(solution(prob, cal))