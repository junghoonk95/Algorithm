case=int(input())
result=[]
p=[0]*500

p[1]=1
p[2]=1
p[3]=1
p[4]=2
p[5]=2
for j in range(case):
    count=int(input())
    for i in range(6,count+1):
        p[i]=p[i-5]+p[i-1]
    result.append(p[count])

for i in result:
    print(i)
