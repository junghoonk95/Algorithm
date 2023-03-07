
def solution(skill, skill_trees):
    answer = -1
    skill_l=list(skill)
    skill_loc=-1
    for i in skill_trees:
        result=True
        skill_loc=-1
        for j in reversed(skill_l):
            if skill_loc!=-1:
                if i.find(j)!=-1:
                    if i.find(j)<skill_loc:
                        skill_loc=i.find(j)
                    else:
                        result=False
                        break
                else:
                    result=False
                    break
            else:
                skill_loc=i.find(j)
        if result==True:
            answer=answer+1
        
    return answer+1
