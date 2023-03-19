def solution(skill, skill_trees):
    global cnt
    
    new_skill_trees = [] 
    skill_check = list(skill)
    for a in skill_trees: 
        a = list(a)
        new_skill_trees.append(a)

    idx_st = [] 
    for i in new_skill_trees: 
        temp = [] 
        for j in range(len(i)): 
            if i[j] in skill_check:
                a = i[j]
                a = str(a)
                # print(a)
                temp.append(skill_check.index(a))
            else:
                temp.append(-1)       

        idx_st.append(temp)
    print('idx_st', idx_st)

    tree_check = []
    ch = []
    cnt = 0
    
    for skill in idx_st: 
        temp = [False for _ in range(len(skill))]
        for i in range(len(skill)):
            if skill[i] == -1:
                temp[i] = True
        check = sum([int(i) for i in temp])

        if check == len(skill):
            cnt+=1 
        print('cnt', cnt)

    for skill in idx_st:
        ch = []
        for i in range(len(skill)):
            if skill[i] >= 0:
                ch.append(skill[i]) 
            # print(ch)
        tree_check.append(ch)
    print('tree_check', tree_check)

    bool_check = [True for _ in range(len(tree_check))]
    for idx, tree in enumerate(tree_check):
        check = False 
        if 0 in tree:        
            for i in range(len(tree)-1): 
                if tree[i] < tree[i+1]: 
                    if (abs(tree[i]-tree[i+1])==1):
                        continue
                    else:
                        bool_check[idx] = False                        
                else:                    
                    bool_check[idx] = False
        else:
            bool_check[idx]=False
        # print(cnt)
        print('bool_check', bool_check)

    answer = sum([int(i) for i in bool_check]) + cnt
    print('answer', answer)
    return answer