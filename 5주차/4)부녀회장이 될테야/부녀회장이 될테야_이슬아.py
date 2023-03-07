case=int(input())
result=[]

for i in range(case):
    k=int(input())
    n=int(input())
    list=[]
    for i in range(n+k+1):
        list.append([])
        list[i].append(1)
        for j in range(1,i):
            list[i].append(list[i-1][j-1]+list[i-1][j])
        if n+2!=0:
            list[i].append(1)
    result.append(list[k+n][k+1])

            
for i in result:
    print(i)
