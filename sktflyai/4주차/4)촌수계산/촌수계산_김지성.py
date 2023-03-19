import sys
n = int(input())
target = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

visited = [False for _ in range(n+1)]

def dfs(x, count):
    '''
    x: 탐색하고자하는 숫자
    count: 촌수
    '''
    # print(x)
    if x == target[1]:
        print(count)
        sys.exit()

    visited[x] = True
    for i in range(len(graph[x])):
        if not visited[graph[x][i]]:
            dfs(graph[x][i], count+1)
    
dfs(target[0], 0)
print(-1)
