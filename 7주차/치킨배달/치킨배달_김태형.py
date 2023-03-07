from collections import deque
from itertools import combinations as cb
import sys
N,M = map(int,input().split()) # M : 폐업하려는 피자집 개수
graph = [list(map(int,input().split())) for _ in range(N)]

houses = deque()
pizzas = deque()

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            houses.append((r,c))
        elif graph[r][c] == 2:
            pizzas.append((r,c))
            
def dist(hr,hc,pr,pc):
    return abs(hr-pr) + abs(hc-pc)
        
n = len(houses)

res = 99999
candidates = [[] for _ in range(M)]

def dfs(L,idx):
    global res
    r,c = pizzas[idx]
    candidates[L] = (r,c)
    # print("현재 L:{},현재 candidates:{}".format(L,candidates))
    if L == M-1:
        tmp_pizza_dist = 0
        for hr,hc in houses:
            min_dist = 99999
            
            for pr,pc in candidates[:L+1]:
                tmp_dist = dist(hr,hc,pr,pc)
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
            tmp_pizza_dist += min_dist
        if tmp_pizza_dist < res:
            res = tmp_pizza_dist           
        return
    
        
    for iidx in range(idx+1,len(pizzas)):
        dfs(L+1,iidx)
       
for j in range(len(pizzas)):
    dfs(0,j)
print(res)