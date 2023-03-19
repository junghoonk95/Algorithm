def solution(skill, skill_trees):
    pre = []
    for S in skill_trees:
        p_s = ''
        for s in S:
            if s  in skill:
                p_s += s
        pre.append(p_s)        
        
    cnt = 0
    for i in pre:
        if i == skill[:len(i)]:
            cnt += 1
                      
    return cnt
