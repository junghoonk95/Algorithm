n=int(input())

point=[0]*301
stair=[0]*301

for i in range(1,n+1):
    stair[i]=(int(input()))

point[1]=stair[1]
point[2]=stair[1]+stair[2]
point[3]=max(stair[1]+stair[3],stair[2]+stair[3])
for i in range(4,n+1):
    point[i]=max(stair[i]+point[i-2], stair[i]+stair[i-1]+point[i-3])

print(point[n])
