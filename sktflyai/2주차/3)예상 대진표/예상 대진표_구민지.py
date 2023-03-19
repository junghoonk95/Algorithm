def solution(n,a,b):
    count=0
    while(True):
        count+=1
        if abs(a-b)==1 and max(a,b)%2==0:
            return count
        a,b=(a+1)//2,(b+1)//2
