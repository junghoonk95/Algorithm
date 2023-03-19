
N,M,V=map(int,input().split())
arr=[[] for _ in range(N)]
dfs=[]
bfs=[]

for i in range(M):
    x,y=map(int,input().split())
    arr[x - 1].append(y)
    arr[y - 1].append(x)

def DFS(v):
    dfs.append(v)
    for i in sorted(arr[v-1]):
        if i not in dfs:
            DFS(i)
    return dfs

def BFS(v):
    queue=[]
    queue.append(v)
    bfs.append(v)
    while queue:
        a=queue.pop(0)
        for i in sorted(arr[a-1]):
            if i not in bfs:
                queue.append(i)
                bfs.append(i)

    return bfs

for i in DFS(V):
    print(i ,end=" ")
print()
for i in BFS(V):
    print(i ,end=" ")





