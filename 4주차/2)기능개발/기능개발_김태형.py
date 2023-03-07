'''
1. 각 기능은 진도 100%일 때 서비스에 반영 가능
2. 각 기능의 개발속도 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있음
    2-1. 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
3. 먼저 배포 되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses,
    각 작업의 개발 속도가 적힌 정수 배열 speeds 주어질 때 각 배포마다 몇 개의 기능 배포되는지 return
'''
# Sol 1.
def done(TMP):
    for _ in TMP:
        if _ != -1:
            return False
    return True

def solution(progresses,speeds):
    l = len(progresses)
    tmp = [[] for _ in range(l)]
    start_idx = 0
    end_idx = None
    answer = []
    while True:
        if done(tmp):
            break
        for i in range(l):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    tmp[i] = progresses[i]
        possible = False
        if tmp[start_idx] and tmp[start_idx] != -1:
            for idx,progress in enumerate(tmp[start_idx:]):
                if not progress:
                    end_idx = start_idx + idx
                    possible = True
                    break
                if idx == len(tmp[start_idx:])-1:
                    end_idx = start_idx+idx+1
                    possible = True
                    
            if possible:
                for idx in range(start_idx,end_idx):
                    tmp[idx] = -1
                answer.append(end_idx-start_idx)
                start_idx = end_idx
    return answer

# # Sol 2. 
# def solution(progresses, speeds):
#     day = 1
#     cnt = 0
#     answer = []
#     while progresses:
#         if progresses[0] + speeds[0]*day >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             cnt += 1
#         else:
#             if cnt > 0:
#                 answer.append(cnt)
#                 cnt = 0
#             day += 1
#     answer.append(cnt)
#     return answer
            
        