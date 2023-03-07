'''
1. 선행 스킬 순서 skill
2. 유저들 만든 스킬트리
-> 가능한 스킬트리 개수 return
'''
def check(skills,skill_tree):
    skills = list(skills) # indexing 위해 list 형태로 변환
    skill_tree = list(skill_tree) # indexing 위해 list 형태로 변환
    # idx_list : 순서대로 스킬을 배웠는지 판별
    # checked : 중간에 건너뛰고 스킬을 배웠는지 판별
    idx_list = []
    checked = [0 for _ in range(len(skills))]
    for i,s in enumerate(skills):
        try:
            idx_list.append(skill_tree.index(s)) # 만약 skill_tree 내에 
                                                 # 주어진 skill 중 하나 존재한다면
                                                 # idx_list에 skill_tree의 s의 위치 저장
            checked[i] = i+1 # checked 저장
        except:
            pass
    for i in range(len(checked)-1):
        if checked[i] == 0 and checked[i+1] != 0:
            return False
    if idx_list == sorted(idx_list):
        return True
    else:
        return False
    
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees: # skill_trees의 각 skill_tree에 대해
        if check(skill,skill_tree): # 만약 check함수에 넣었을때 true를 return하면
            answer += 1 # + 1
    return answer

# solution("CBD","AECB")