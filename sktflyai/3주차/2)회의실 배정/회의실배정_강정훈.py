N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

new_time=sorted(arr,key=lambda x:x[0])
new_time=sorted(new_time,key=lambda x:x[1])
end = 0 
cnt = 0 

for i, j in new_time:
  if i >= end:
    cnt=cnt+ 1
    end=j

print(cnt)
