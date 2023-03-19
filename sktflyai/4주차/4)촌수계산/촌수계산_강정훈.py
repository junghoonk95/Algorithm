from collections import deque


N = int(input())

T1, T2 =map(int,input().split())
m=int(input())

arr=[[] for _ in range(N+1)]
cnt=0
count=[0 for i in range(N+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(T1,T2):

    q=deque()
    q.append(T1)
    visit=[]

    while q:

        target=q.popleft()
        visit.append(target)

        if target ==T2:
            break
        for i in arr[target]:
            if i not in visit:
                count[i]=count[target]+1
                q.append(i)

                
    if count[T2]==0: 
        print(-1)
    else: 
        print(count[T2])

bfs(T1,T2)
#print(count[T2])
