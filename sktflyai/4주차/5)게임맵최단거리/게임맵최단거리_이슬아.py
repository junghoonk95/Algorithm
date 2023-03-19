from collections import deque
def solution(maps):
    answer = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(maps)
    m=len(maps[0])
    x,y=0,0
    dq=deque()
    dq.append((x,y))
    
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                dq.append((nx,ny))
    if maps[n-1][m-1]!=1:
        answer=maps[n-1][m-1]
    else:
        answer=-1
    return answer
