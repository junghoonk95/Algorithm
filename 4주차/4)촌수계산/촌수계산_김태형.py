n = int(input())
s,e = map(int,input().split())
m = int(input())
relationships = [[] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    relationships[a].append(b)
    relationships[b].append(a)

cnt = 0
visited[s-1] = 1
is_possible = False

def dfs(now):
    global cnt,is_possible
    if is_possible:
        return
    if now == e-1:
        print(cnt)
        is_possible = True
        return
    for i in relationships[now]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            dfs(i)
            cnt -= 1
            visited[i] = 0

dfs(s-1)

if not is_possible:
    print(-1)