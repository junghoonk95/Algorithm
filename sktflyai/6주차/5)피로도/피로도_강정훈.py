from itertools import*

def solution(k, dungeons):
    arr=list(permutations(dungeons,len(dungeons))) ## 모든 경우의 수 
    sol=[]
    for i in arr:
        exhausted=k   # 피로도 = k = 80
        cnt=0         # 방문 던전
        for j in i:    # ([80, 20], [50, 40], [30, 10])  / 
            if j[0]<=exhausted:  #j[0] =80 <= 80
                exhausted=exhausted-j[1] 피로도= 80 - 20
                cnt=cnt+1  #cnt+1
        sol.append(cnt)
        
    print(sol)
    return max(sol)
  
'''
arr=
([80, 20], [50, 40], [30, 10])
([80, 20], [30, 10], [50, 40])
([50, 40], [80, 20], [30, 10])
([50, 40], [30, 10], [80, 20])
([30, 10], [80, 20], [50, 40])
([30, 10], [50, 40], [80, 20])
'''
