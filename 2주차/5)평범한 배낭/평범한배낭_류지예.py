# 에러ㅓ...
n, k = map(int, input().split())
w_list = []
v_list = []
for _ in range(n):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

# vw_dict = {v_list[i] : w_list[i] for i in range(n)}

answer = 0
for i in range(n):
    for j in range(1, n-i):
        if w_list[i] + w_list[i+j] <= k:
            if answer < v_list[i] + v_list[i+j]:
                answer = v_list[i] + v_list[i+j]

print(answer)
