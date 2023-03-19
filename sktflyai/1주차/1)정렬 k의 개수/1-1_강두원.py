def solution(i, j, k):   
    return sum(list(map(lambda x: str(x).count(str(k)), range(i, j+1))))
