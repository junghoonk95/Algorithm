n,m = map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
sim=[]
sol=0
ans=[]
for i in range(n):
    sim.append(arr[i])
    sim.append(tuple(zip(*arr))[i])
print(len(sim))
for i in range(len(sim)):
    c==0
    while c==len(sim[i]):
