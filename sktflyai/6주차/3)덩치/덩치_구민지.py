n = int(input())

inputs =[list(map(int,input().split())) for _ in range(n)]

ranks=[]
for i in range(len(inputs)):
    rank=1
    for j in range(len(inputs)):
        if i!=j:
            if inputs[j][0]>inputs[i][0] and inputs[j][1]>inputs[i][1]:
                rank+=1
                
    ranks.append(rank)
    
for r in ranks:
    print(r,end=' ')
