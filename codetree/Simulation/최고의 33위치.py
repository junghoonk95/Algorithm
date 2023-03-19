N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]

a=[]
for i in range(N-2):
    for j in range(N-2):
        cnt=0
        for x in range(i,i+3):
            for y in range(j,j+3):
                if arr[y][x]==1:
                    cnt=cnt+1
        a.append(cnt)

print(max(a))
