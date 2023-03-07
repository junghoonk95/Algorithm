N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

cntMinus, cntZero, cntOne = 0, 0, 0

def divideConquer(x, y, N):
    global cntMinus, cntZero, cntOne
    cur = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if cur != paper[i][j]:
                for m in range(3):
                    for n in range(3):
                        divideConquer(x + m*(N//3), y + n*(N//3), N//3)
                return 
    
    if cur == -1:
        cntMinus += 1
    elif cur == 0:
        cntZero += 1
    elif cur == 1:
        cntOne += 1

divideConquer(0, 0, N)
print(cntMinus)
print(cntZero)
print(cntOne)
            
