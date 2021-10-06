def prime_factorization(k):
    k_list = []
    while k > 1:
        for i in range(2, k+1):
            if k % i == 0:
                k_list.append(i)
                k = k // i
                break
    return k_list


def solution(a, b):
    a_list = prime_factorization(a)
    b_list = prime_factorization(b)
    and_list = []
    while True:
        idx = -1
        for i in range(len(a_list)):
            if a_list[i] in b_list:
                idx = b_list.index(a_list[i])
                break
        if idx != -1:
            and_list.append(b_list.pop(idx))
            del a_list[a_list.index(and_list[-1])]
            continue
        break
    gcd, lcm = 1, 1
    for elem in and_list:
        gcd *= elem
    for elem in and_list+a_list+b_list:
        lcm *= elem
    return "{}\n{}".format(gcd,lcm)


a, b = map(int, input().split())
print(solution(a, b))
