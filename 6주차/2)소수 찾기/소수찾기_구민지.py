import itertools
import math

def solution(numbers):
    prime_nums=[]
    for i in range(1,len(numbers)+1):
        # permutations 조합 , set 중복 제거
        nums = set(itertools.permutations(numbers,i))
        for n in nums:
            n=int(''.join(n))
            if primeNum(n):
                prime_nums.append(n)
                
    return len(set(prime_nums))
            
# 소수 판별            
def primeNum(x):
    if x < 2 :
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i ==0:
            return False
    return True
    
