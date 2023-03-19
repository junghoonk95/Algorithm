T=int(input())
df=[0 for i in range(101)]
df[0]=1
df[1]=1
df[2]=1
for i in range(3,100):
    df[i]=df[i-3]+df[i-2]

print(df)
for i in range(T):
    N=int(input())
    print(df[N-1])
