N = int(input())
table = []
for _ in range(N):
    table.append(tuple(map(int,input().split())))

# print(table)

st = et = 0
cnt = 0
table.sort(key=lambda x:(x[1],x[0]))

for s,e in table:
    if et <= s and et <= e:
        et = e
        st = s
        cnt += 1

# print(table)
print(cnt)