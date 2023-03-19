import math
def solution(n,a,b):
    maxtime=int(math.log2(n))
    answer=0
    for i in range(maxtime):
        print(i)
        if a>b:
            answer=answer+1
        elif a<b:
            answer=answer+1
        a=a//2+a%2
        b=b//2+b%2
    return answer
