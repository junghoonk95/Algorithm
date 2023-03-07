def solution(skill, skill_trees):
    new_skill=[]  
    new=[] 
    poss=[]   #skill을 짤라서 넣을 list
    
    for i in range(len(skill)):  #skill 경우의수 ex. CBD-> C,CB,CBD
        k=skill[0:i+1]
        poss.append(k)
          
    for t in skill:   #skill 하나씩 CBD-> C,B,D
        new.append(t)
        
    for i in skill_trees: # skll_tree 
        s=""
        for j in range(len(i)):  #각스킬에서 CBD만 추출 하여 new_skill에 저장
            if i[j] in new:
                s=s+i[j]
        new_skill.append(s)       #결과는 ex. 	['BCD', 'CBD', 'CB', 'BD']
    print(new_skill)
    cnt1=0
    for i in new_skill: # poss에 있거나 빈칸 <skill이외> 면 +1
        if i in poss or i=="":
            cnt1=cnt1+1
            
    return cnt1
