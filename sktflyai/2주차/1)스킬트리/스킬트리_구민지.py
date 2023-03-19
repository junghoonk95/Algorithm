def solution(skill,skill_trees):
    count=0
    for skill_tree in skill_trees:
        temp=""
        for s in skill_tree:
            if s in skill:
                temp+=s

        if temp == skill[:len(temp)]:
            count+=1

    return count
