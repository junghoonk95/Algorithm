n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
z, o, m = 0, 0, 0

def div_paper(k, p):
    global z, o, m
    check = False # 전부 같은 숫자인지 확인하는 용도
    if k == 1: # 크기가 1인 경우 밑의 조건문을 시행하지 않고 바로 확인
        if p[0][0] == 0: z += 1
        elif p[0][0] == 1: o += 1
        elif p[0][0] == -1: m += 1
    else: # 크기가 1보다 큰 경우
        for i in range(k):
            for j in range(k-1):
                if p[i][j] != p[i][j+1]: # 같은 행 확인
                    check = True
        if not check: # 만약 행이 모두 같다면 열까지 확인
            for i in range(k-1):
                for j in range(k):
                    if p[i][j] != p[i+1][j]: # 같은 열 확인
                        check = True
        if not check: # 같은 경우
            if p[0][0] == 0: z += 1
            elif p[0][0] == 1: o += 1
            elif p[0][0] == -1: m += 1
        else: # 다른 경우 9개로 분할해서 재귀
            tmp = [p[i][0:k//3] for i in range(0, k//3)]
            div_paper(k//3, tmp)
            tmp = [p[i][k//3:2*(k//3)] for i in range(0, k//3)]
            div_paper(k//3, tmp)
            tmp = [p[i][2*(k//3):k] for i in range(0, k//3)]
            div_paper(k//3, tmp)
            tmp = [p[i][0:k//3] for i in range(k//3, 2*(k//3))]
            div_paper(k//3, tmp)
            tmp = [p[i][k//3:2*(k//3)] for i in range(k//3, 2*(k//3))]
            div_paper(k//3, tmp)
            tmp = [p[i][2*(k//3):k] for i in range(k//3, 2*(k//3))]
            div_paper(k//3, tmp)
            tmp = [p[i][0:k//3] for i in range(2*(k//3), k)]
            div_paper(k//3, tmp)
            tmp = [p[i][k//3:2*(k//3)] for i in range(2*(k//3), k)]
            div_paper(k//3, tmp)
            tmp = [p[i][2*(k//3):k] for i in range(2*(k//3), k)]
            div_paper(k//3, tmp)

div_paper(n, paper)
print(m)
print(z)
print(o)