from itertools import*
n,m=map(int,input().split())

arr=[list(map(int,input().split())) for i in range(n)]

nx1=[0,1,1,1,0,-1,-1,-1,-1,0]
ny1=[1,1,0,-1,-1,-1,0,1,0,1]
nx2=[1,1,1,0,-1,-1,-1,0,1,0]
ny2=[1,0,-1,-1,-1,0,1,1,0,-1]

sol1=0

for j in range(n):  #y
    for k in range(m):  #x
        for i in range(10):
            if j+ny1[i]<0 or j+ny1[i]>=n or j+ny2[i]<0 or j+ny2[i]>=n or k+nx1[i]<0 or k+nx1[i]>=m or k+nx2[i]<0 or k+nx2[i]>=m:
                continue
            dx=k+nx1[i]
            dx1=k+nx2[i]
            dy=j+ny1[i]
            dy1=j+ny2[i]
        
            sol1=max(sol1,arr[j][k]+arr[dy][dx]+arr[dy1][dx1])
        
        
        
print(sol1)
