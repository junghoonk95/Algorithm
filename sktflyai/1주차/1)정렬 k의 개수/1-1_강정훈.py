def solution(i, j, k):
    n=""
    for t in range(i,j+1):
        n=n+str(t) 
    sol=0
    for i in n:
        if i==str(k):
            sol=sol+1
    return sol
