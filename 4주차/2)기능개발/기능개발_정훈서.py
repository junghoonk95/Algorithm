def solution(progresses, speeds):
    answer = []
    when = []
    count = 1
    length = len(progresses)
    
    for i in range(length): # 작업 별 끝날 때까지 걸리는 시간을 담은 배열
        for k in range(101):
            if progresses[i] + k*speeds[i] >= 100:
                when.append(k)
                break
    
    if length == 1: # 작업이 한 개인 경우
        answer.append(count)
    else:
        cur = when[0] # 초기값
        for i in range(1, length):
            if when[i] > cur:
                answer.append(count)
                cur = when[i]
                count = 1
            else:
                count += 1
            
            if i == length - 1: # 작업이 2개 이상이고 i가 마지막인 경우
                answer.append(count)
    return answer