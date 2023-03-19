n, m = int(input()), int(input())
input_li = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]

for i in input_li:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

visited = [False for _ in range(n+1)]

def dfs(graph, v):
    visited[v] = True
    for x in graph[v]:
        if not visited[x]:
            dfs(graph, x)
    return visited.count(True) - 1

print(dfs(graph, 1))