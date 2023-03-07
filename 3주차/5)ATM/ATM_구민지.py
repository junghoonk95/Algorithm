N = int(input())
inputs=list(map(int,input().split()))

ans=0
inputs.sort()
for i in range(1,len(inputs)+1):
    ans+=sum(inputs[:i])
    
print(ans)
