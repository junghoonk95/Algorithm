# pop(0)은 O(N) 왜냐면 pop은 [0,1,2,3,4]라고 하면 맨앞꺼 빼면 한칸씩 앞으로 땡겨주는 원리

#하지만 deque의 popleft를 쓰면 O(1) -> deque는 큐지만 선입 선출 (FIFO : First In First Out) 개념이 없음
# 그래서 deque을 안쓰면 효율성테스트에서 0점 나올 수 있음

from collections import*
def solution(people, limit):
    cnt=0
    new_arr = deque(sorted(people, reverse=True).copy()) #데큐 사용 파이썬 모듈
    while len(new_arr)!=0:  #new_arr가 empty될까지
        if len(new_arr)==1: # 만약 1이면 그냥+1 혼자니까
            cnt=cnt+1
            new_arr.pop()
        
        elif new_arr[0]+new_arr[-1] <= limit: #맨앞과 맨뒤 합이 limit보다 작거나 같으면 둘다 뺌
            new_arr.popleft()
            new_arr.pop()
            cnt=cnt+1
        else:
            new_arr.popleft() #아니면 맨앞만 빼주기
            cnt=cnt+1
    return cnt
    
  ##############################################정확도는 맞지만 효율성 0점 그이유는 데큐 안써서 통과 안된 코드
    
    cnt=0
    new_arr=sorted(people, reverse=True).copy()

    while new_arr!=[] : 
        if len(new_arr)==1:
            cnt=cnt+1
            break
        
        elif new_arr[0]+new_arr[-1] <= limit:
            new_arr.pop(-1)
            new_arr.pop(0)
            cnt=cnt+1
        else:
            new_arr.pop(0)
            cnt=cnt+1
    return cnt
        
            
