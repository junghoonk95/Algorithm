N,D=map(int,input().split())
arr= [[] for i in range(10001)]
dist= [i for i in range(D+1)]

for i in range(N):
    s,e,leng= map(int,input().split())
    arr[s].append((e,leng))

for i in range(D+1):
    if i!=0:
        dist[i]=min(dist[i],dist[i-1]+1)
    for j in arr[i]: # e, leng  (50,10) 150 0

        if j[0]<=D: # 지름길 <고속도로
            # print(j, D, dist[i], dist[j[0]])
            if dist[j[0]]> j[1] +dist[i]: # 기존 고속도로 >  지름길 길이+ 시작점까지 100> 10+10 ,140>90+30
                print(dist[j[0]],j[1],dist[i],i)
                print(dist)
                dist[j[0]]=j[1]+dist[i]  # 지름길

print(dist[D])
