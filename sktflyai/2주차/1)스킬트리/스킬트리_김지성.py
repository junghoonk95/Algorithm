def solution(skill, skill_trees):
    # temp : 여기다가 스킬트리에 해당하는 문자 순서대로 넣어주기
    # 넣은 문자가 순서에 맞는지 안 맞는지 확인하기
    # 순서에 맞다면 answer 증가
    answer =0
    
    for i in skill_trees:
        temp =''
        for ch in i:
            if ch in skill:
                temp+=ch
                
        if skill[:len(temp)]==temp:
            answer +=1
    
    return answer
