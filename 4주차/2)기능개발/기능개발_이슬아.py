def solution(progresses, speeds):
    daylist = []
    first=0
    day=0
    answer=[]
    
    while 1:
        for i in range(len(progresses)):
            if first<len(progresses) and progresses[first]>=100:
                daylist.append(day)
                first=first+1
            else:    
                for j in range(len(progresses)):
                    progresses[j]=progresses[j]+speeds[j]  
                day=day+1
        if first==len(progresses):
            break
    result=sorted(list(set(daylist)))
    for i in result:
        answer.append(daylist.count(i))

    return answer
