n=int(input())

d=[0]*(n*3)
d[1]=0

for i in range(2,n+1):
    if i%6==0:
        d[i]=min(d[i-1],d[i//2],d[i//3])+1
    elif i%2==0:
        d[i]=min(d[i-1],d[i//2])+1
    elif i%3==0:
        d[i]=min(d[i-1],d[i//3])+1
    else:
        d[i]=d[i-1]+1

print(d[n])
