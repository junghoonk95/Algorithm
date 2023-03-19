N,P= map(int,input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr=sorted(arr,reverse=True)

count=0
for i in arr:
    if P==0:
        break

    else:
        remain= P%i
        count= count+ P//i
        P=remain

print(count)



