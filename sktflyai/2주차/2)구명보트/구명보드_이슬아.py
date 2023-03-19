from collections import deque
def solution(people, limit):
    answer = 0
    dq=deque(sorted(people))
    while dq:
        maxindex=dq.pop()
        if len(dq)>0:      
            minindex=dq.popleft()
            if minindex+maxindex>limit:
                dq.appendleft(minindex)
        answer=answer+1
    return answer
