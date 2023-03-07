
N=int(input())
arr= [list(map(int,input().strip())) for i in range(N)]
end=[[0 for _ in range(N)] for _ in range(N)]
visit=arr.copy()

sol=[]
def dfs(x,y):
    global visit,cnt_in
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit[x][y]=0
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        if nx>=N or nx<0 or ny>=N or ny<0:
            continue
        elif arr[nx][ny] !=0 and visit[nx][ny]!=0:
            visit[nx][ny]=0
            cnt_in=cnt_in+1
            dfs(nx,ny)

while visit != end:
    for c in range(N):
        for r in range(N):
            if visit[r][c]!=0:
                cnt_in = 1
                dfs(r,c)
                sol.append(cnt_in)

print(len(sol))
sol=sorted(sol)
for i in sol:
    print(i)
