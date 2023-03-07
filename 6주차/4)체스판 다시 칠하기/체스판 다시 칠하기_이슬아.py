

chess=[]
h,w=map(int,input().split())
chess=[[]*w]*h
result=[]

for i in range(h):
    s=input()
    chess[i]=(list(s))

def checkChess(x,y):
    result=[]
    last=""
    for v in range(2):
        check=0
        if v==0:
            last='W'
        else:
            last='B'
        for i in range(x,x+8):
            for j in range(y,y+8):
                if last=='W' and chess[i][j]=='W':
                    check=check+1
                    last='B'
                elif last=='B' and chess[i][j]=='B':
                    check=check+1
                    last='W'
                else:
                    last=chess[i][j]
            if last=="W":
                last="B"
            else:
                last="W"
        result.append(check)
    return min(result)


for s in range(h-7):
    for k in range(w-7):
        result.append(checkChess(s,k))

print(min(result))
