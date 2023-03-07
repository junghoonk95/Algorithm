from itertools import permutations
from itertools import combinations

def eratosthenes(num):
    check = [False, False] + [True] * (num-1)
    res = []
    for i in range(2, num+1):
        for j in range(i*2, num+1, i):
            if check[j] == True:
                check[j] = False
    for i, v in enumerate(check):
        if v:
            res.append(i)
    return res

def solution(numbers):
    comb = []
    for i in range(1, len(numbers)+1):
        for j in combinations(numbers, i):
            comb.append(list(j))
    perm = set()
    for i in comb:
        for j in permutations(i):
            perm.add(j)
    res = set()
    for i in perm:
        res.add(int(''.join(i)))
    res = list(res)

    prime_num = eratosthenes(max(res))
    answer = 0
    for i in res:
        if i in prime_num:
            answer += 1
    return answer
