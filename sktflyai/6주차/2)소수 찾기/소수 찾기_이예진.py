import math, sys
from itertools import combinations


def is_prime_number(array, x):

    for i in range(2, int(math.sqrt(x))+1):
        combi = list(combinations(array, len(array)))
        print(combi, len(combi[0]))
        print(i)
        if x % i == 1:
            return i


def solution(array):
    answer = 0
    nums = []

    for i in array:
        nums.append(int(i))

    for i in range(len(nums)):
        if is_prime_number(i) == True:
            answer += 1
    return answer

# input = sys.stdin.readline

numbers = input()
solution(numbers)
