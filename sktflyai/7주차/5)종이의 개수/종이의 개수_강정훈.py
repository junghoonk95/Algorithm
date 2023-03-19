N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
arr=[]
mone=0
zero=0
one=0
def cut(x, y, N) :
    global mone,zero,one
    c=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if c!=paper[i][j]:
                for q in range(3):
                    for z in range(3):
                        cut(x + q * (N//3), y + z * (N//3), N//3)

                return
    if c == -1:
        mone= mone+1
    elif c== 0:
        zero=zero+1

    elif c== 1:
        one=one+1

cut(0,0,N)

print(mone,zero,one,sep="\n")
