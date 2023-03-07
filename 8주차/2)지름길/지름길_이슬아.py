//실패...

m, n = map(int, input().split())
k = 0                
INF = 1e8

graph = [[] for _ in range(n+2)] 

distance = [INF] * (n+2)

for _ in range(m):
    u, v, w = map(int, input().split()) 
    if v>n or (v-u)<w:
        continue
    else:
        graph[u].append((v, w))            

for i in range(n):
    graph[i].append((i+1,1))

import heapq

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) 

    if distance[now] < dist:
      continue            

    for i in graph[now]:     
      if dist+i[1] < distance[i[0]]: 
        distance[i[0]] = dist+i[1]   
        heapq.heappush(q, (dist+i[1], i[0]))

dijkstra(k)
count = 0
max_distance = 0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)

print(max_distance)
