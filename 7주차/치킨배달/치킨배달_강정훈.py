from itertools import combinations

N,M = map(int,input().split())
arr=[list(map(int,input().split())) for i in range(N)]
sol=[]
home=[]
chic=[]
def dis(r1,r2,c1,c2):
    return abs(r1-r2)+abs(c1-c2)

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            home.append([i,j])
        if arr[i][j]==2:
            chic.append([i,j])

all_chic=list(combinations(chic,M))
#print(home)   # [[0, 2], [1, 4], [2, 1], [3, 2]]
#print(chic)   # [[1, 2], [2, 2], [4, 4]]
for i in all_chic:
    tot=0
    for r1,c1 in home:
        dist=9999
        for r2,c2 in i:
            # print(r2,c2)
            dist=min(dist,dis(r1,r2,c1,c2))
        tot=tot+dist
    sol.append(tot)

print(min(sol))
