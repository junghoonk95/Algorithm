def solution(n,a,b):
    cnt=0
    while True: 
        if a!=b: # a b 가 같지 않으면 cnt+1, a+1하는 이유 12/34/56/78 ->23/45/67/89 ->11/22/33/44
            cnt=cnt+1
            a= (a+1)//2
            b= (b+1)//2
        else:
            break
    return cnt
