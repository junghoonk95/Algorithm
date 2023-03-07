import math
def solution(progresses, speeds):
    complete = []
    for i in range(len(progresses)):
        complete.append(math.ceil((100 - progresses[i])/speeds[i]))

    answer = []
    cnt = 1
    v = complete[0]
    for i in range(1, len(complete)):
        if complete[i] <= v:
            cnt += 1
        else:
            v = complete[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer