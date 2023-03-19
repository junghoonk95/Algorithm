N = int(input())
paper = [list(map(int,input().strip())) for _ in range(N)]
arr=[]
def quadt(x, y, N) :
    c=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if c!=paper[i][j]:
                arr.append("(")
                quadt(x,y,N//2)
                quadt(x, y+N//2, N//2)
                quadt(x+N//2, y, N//2)
                quadt(x+N//2, y+N//2, N//2)
                arr.append(")")
                return
    if c == 0:
        arr.append(0)
    else:
        arr.append(1)

quadt(0,0,N)

for i in arr:
    print(i,end="")
