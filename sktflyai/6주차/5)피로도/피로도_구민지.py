import itertools

def solution(k,dungeons):
    
    p_dungeons = list(itertools.permutations(dungeons))

    results=[]
    for dungeons in p_dungeons:
        current_p = k
        cnt=0
        for min_p,p in dungeons:
            if current_p >= min_p:
                current_p-=p
                cnt+=1
            else:
                continue
        results.append(cnt)
        
    return max(results)
    
