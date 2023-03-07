n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = ""
# 4개로 분할해서 확인
def check_graph(m, g): # m = (n/2)^k, g = 그래프 중 확인할 부분
    global result
    check = 0
    for i in range(m):
        for j in range(m):
            check += g[i][j]
    if check == 0: # 전부 0이라면
        result += "0"
    elif check == m*m: # 전부 1이라면
        result += "1"
    else: # 0과 1이 둘 다 있다면
        result += "("
        quarter_graph = [g[i][0:m//2] for i in range(0, m//2)]
        check_graph(m//2, quarter_graph)
        quarter_graph = [g[i][m//2:m] for i in range(0, m//2)]
        check_graph(m//2, quarter_graph)
        quarter_graph = [g[i][0:m//2] for i in range(m//2, m)]
        check_graph(m//2, quarter_graph)
        quarter_graph = [g[i][m//2:m] for i in range(m//2, m)]
        check_graph(m//2, quarter_graph)
        result += ")"

check_graph(n, graph)
print(result)