N,K=map(int,input().split())

inputs= [input() for _ in range(N)]
inputs=list(map(int,inputs))
        
i=len(inputs)-1
cnt=0
while(K!=0):
    if inputs[i]<=K:
        q,K = divmod(K,inputs[i])
        cnt+=q
    i-=1       
    
print(cnt)
