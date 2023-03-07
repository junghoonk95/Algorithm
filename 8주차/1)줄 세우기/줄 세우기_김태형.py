# https://freedeveloper.tistory.com/390

from collections import deque

# N : 노드 개수, M : 간선 개수
N,M = map(int,input().split())

# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (N+1)

# 각 노드에 연결된 간선 정보 담기 위한 연결 리스트 초기화
graph = [[] for i in range(N+1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(M):
    a,b = map(int,input().split())

    # 노드 a -> b 이동 가능
    graph[a].append(b)

    # b 진입 차수 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1,N+1):
        if not indegree[i]:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()



