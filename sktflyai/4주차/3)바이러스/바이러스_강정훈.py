C=int(input())
net=int(input())
arr=[[] for _ in range(C+1)]
visit=[]


for i in range(net):
    a,b=map(int,input().split())

    arr[a].append(b)
    arr[b].append(a)
cnt=0
def dfs(v): # dfs 신규 장소 마다 visit에 넣어주기
    global cnt
    for i in arr[v]:
        if i not in visit:
            visit.append(i)
            dfs(i)
        else:
            cnt=cnt+1
    return visit
dfs(1)
print(len(visit)-1)  #1은 빼주기
