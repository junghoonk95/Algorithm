def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        container = []
        standard = -1
        continuous = True
        cnt = 1
        for j in skill:
            if j not in i:
                continuous = False
            elif j in i and continuous:
                container.append(j)
            else:
                cnt = 0
                break
            
        for k in container:
            idx = i.index(k)
            if idx > standard:
                standard = idx
                continue
            else:
                cnt = 0
        answer += cnt
    return answer
