N,K = map(int,input().split())

A = [int(input()) for _ in range(N)]

cnt = 0
for coin in A[::-1]:
    if K == 0:
        break
    if coin <= K:
        
        tmp = K // coin
        cnt += tmp
        # print(tmp,cnt,coin)
        K %= coin
    
print(cnt)