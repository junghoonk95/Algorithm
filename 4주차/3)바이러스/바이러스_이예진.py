N = int(input())
M = int(input())

visited = [False]*(N+1)
graph = [[0]*(N+1) for _ in range(N+1)]
cnt = 0

for _ in range(M):
    x, y = map(int, input().split())
    """
   sys.stdin.readline().rstrip().split()   
   >> ValueError: not enough values to unpack (expected 2, got 0)
   
    """
    graph[x][y] = 1
    graph[y][x] = 1
    
def dfs(V):
    global cnt
    visited[V] = True    
    print(V, end = '')    
    for i in range(1, N+1):
        if visited[i] == False and graph[V][i] == 1:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
