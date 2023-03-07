import math
from itertools import permutations

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    ans_list = []
    num_list = list(numbers)
    for i in range(1, len(num_list)+1):
        for num_string in permutations(num_list, i):
            num = int(''.join(map(str, num_string)))
            if num == 0 or num == 1:
                continue
            if isPrime(num):
                ans_list.append(num)
    return len(set(ans_list))