def dfs(v):
    print(v, end=' ')
    # 방문 노드 체크
    visit[v] = 1
    for i in range(1, n + 1):
    	# 방문한적 없는 인접 노드 방문
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
	# 시작 노드 큐에 추가
    queue = [v]
    # 방문 노드 체크
    visit[v] = 0
    # 큐가 빌때까지 반복
    while (queue):
    	# 시작 노드 추출
        v = queue[0]
        print(v, end=' ')
        # 시작 노드 제거
        del queue[0]
        for i in range(1, n + 1):
        	# 방문한적 없는 인접 노드 방문
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())
# 행 열 번호를 사용하기위해 0번째 인덱스 0으로 초기화
s = [[0] * (n + 1) for i in range(n + 1)]
# 방문 체크 리스트
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

dfs(v)
print()
bfs(v)
