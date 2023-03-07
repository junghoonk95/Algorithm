n, m, v = map(int, input().split())

lst = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
    lst[a].sort()
    lst[b].sort()

visited = [False] * len(lst)

def dfs(graph, node, visited):
    print(node, end = ' ')
    visited[node] = True

    for neighbor in graph[node]:
        if visited[neighbor] == False:
            dfs(graph, neighbor, visited)

dfs(lst, v, visited)
print()
from collections import deque

def bfs(graph, node):
    deq = deque()

    visited = [False] * len(graph)

    deq.appendleft(node)
    visited[node] = True
    res = [node]
    while len(deq) > 0:
        node = deq.pop()
        for i in graph[node]:
            if visited[i] == False:
                deq.appendleft(i)
                res.append(i)
                visited[i] = True
    return res
print(*bfs(lst, v))
