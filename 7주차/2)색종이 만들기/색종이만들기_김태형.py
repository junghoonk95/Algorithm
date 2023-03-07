def color(x,y,n):
    global white,blue     
    check=graph[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=graph[i][j]:     
                color(x,y,n//2)      
                color(x,y+n//2,n//2)     
                color(x+n//2,y,n//2)       
                color(x+n//2,y+n//2,n//2) 
                return

    if check==0:
        white+=1
        return
    else:
        blue+=1
        return


N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

white,blue=0,0

color(0,0,N)
print(white)
print(blue)