def solution(N,a,b):
    people = [i for i in range(1,N+1)] # 대회 참여하는 사람 생성
    
    answer = 0
    is_break = False
    
    while not is_break: # break 하기 전까지 while문
        answer += 1
        tmp = []
        for i in range(0,len(people),2): # 2명씩 group
            group = people[i:i+2] # 2명씩 group
            if [a,b] == group or [b,a]==group: # 찾았으면 break
                is_break = True
                break
            if a in group: # group 내에 a 있으면
                tmp.append(a) # tmp에 a를 추가
            elif b in group: # group 내에 b 있으면
                tmp.append(b) # tmp에 b를 추가
            else: # a,b 둘 다 없으면
                tmp.append(group[0]) # 임의의 사람 추가
        people = tmp
    return answer


