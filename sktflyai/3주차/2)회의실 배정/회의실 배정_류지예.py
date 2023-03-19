n = int(input())

t_list = []
for _ in range(n):
    t_list.append(list(map(int, input().split())))
t_list.sort()

cnt = 1
start, finish = t_list[0][0], t_list[0][1]
for i in range(1, n):

    s, f = t_list[i][0], t_list[i][1]
    if f < finish:
        finish = f
    elif finish <= s:
        start = s
        finish = f
        cnt += 1
        
print(cnt)
