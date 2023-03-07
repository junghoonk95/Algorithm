from itertools import*
import math
def getprime(x):
    if x<=1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    anw=[]
    cnt=0
    num=[]
    answer=[]
    for i in numbers:
        num.append(i)
        
    for i in range(1,len(numbers)+1):
        answer.extend(list(permutations(num,i)))
    answer=list(set(answer))
    
    for i in answer:
        obj=""
        for j in i:
            obj=obj+j
        print(int(obj))
        if getprime(int(obj))==True:
            anw.append(int(obj))
            
    print(sorted(list(set(anw))))
            
            
    return len(list(set(anw)))


# [2, 3, 11, 13, 23, 31, 113, 131, 211, 311, 1123, 1213, 1231, 1321, 2113, 2131, 2311, 3121]
