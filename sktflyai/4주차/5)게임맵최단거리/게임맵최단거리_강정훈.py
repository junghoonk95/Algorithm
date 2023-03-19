def solution(maps):
    # visit=[]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    n=len(maps[0]) # 가로nx
    m=len(maps)    # 세로ny
    visit=maps.copy()
    cnt=1

    sol=[]

    def dfs(x,y):
        nonlocal cnt, sol
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=n or ny>=m or nx<0 or ny<0 or visit[ny][nx]==0 or maps[ny][nx]==0 :
                continue
            elif ny==m-1 and nx ==n-1:
                cnt=cnt+1
                sol.append(cnt)
                
            elif maps[ny][nx]==1 and visit[ny][nx]==1:
                visit[ny][nx]=0
                cnt=cnt+1
                dfs(nx,ny) 
                

    dfs(0,0)
    if sol==[]:
        return -1
    else:
        return min(sol)
    
#################

def solution(maps):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q=[(0,0,0)]
    N,M=len(maps),len(maps[0])
    visit=[[0 for i in range(M)] for i in range(N)]
    
    while q:
        x,y,cnt=q.pop(0)
        if x==M-1 and y==N-1:
            return cnt+1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            elif visit[ny][nx]==0 and maps[ny][nx]==1:
                visit[ny][nx]=1
                q.append((nx,ny,cnt+1))
        
        

    return -1










