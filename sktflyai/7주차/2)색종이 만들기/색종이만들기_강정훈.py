N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

cnt0=0
cnt1=0

def cut(x, y, N) :
    global cnt0,cnt1
    c=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if c!=paper[i][j]:
                cut(x,y,N//2)
                cut(x+N//2, y, N//2)
                cut(x, y+N//2, N//2)
                cut(x+N//2, y+N//2, N//2)
                return
    if c == 0:
        cnt0=cnt0+1
    else:
        cnt1=cnt1+1

cut(0,0,N)
print(cnt0)
print(cnt1)
