def solution(progresses, speeds):
    q=progresses
    sol=[]
    while q: #q가 [] 될때까지
        cnt=0
        tem=[] # 임시
        while q[0]<100:    # 맨앞이 100보다 작으면 하루추가
            for i in range(len(q)):  
                q[i]=q[i]+speeds[i]  
        cnt=0
        tem=[]
        for j in q:  #맨앞 100보다 커졌을때 다음께 100보다 작으면 break
            if j<100:
                break
            else:
                tem.append(j)  # 아니면 임시에 j 추가
            
        for k in tem:   #임시 만큼 q에서 빼주기
            q.pop(0)
            speeds.pop(0)
            cnt=cnt+1
        sol.append(cnt) #임시 갯수 sol에 추가

    return sol
    
    
    
    
    
    
    
    
    
