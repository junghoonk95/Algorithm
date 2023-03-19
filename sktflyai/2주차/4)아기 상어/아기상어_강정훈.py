### 포기....

#머리는 BFS를 사용해야하는것을 알았지만 구현에서 포기...
#의도: 처음 1~6위치 람다서치로 조건에 맞는 순서 정렬하여
#for 문 돌려서 최단경로 찾으려고 



N=int(input())

arr= []

for i in range(N):
    arr.append(list(map(int,input().split())))

init=[[] for i in range(7)]

for i in range(N):
    for j in range(N):
        print(arr[i][j])
        if arr[i][j] != 9 and arr[i][j]!=0:
            print(arr[i][j])
            init[arr[i][j]].append((j,i))

init_c=init.copy()
print(init_c[1][0])
for i in init:
    init_c[i].sort(key= lambda x:x[i][0])

print(init_c)
