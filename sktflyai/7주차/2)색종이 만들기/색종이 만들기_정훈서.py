n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_paper = 0
blue_paper = 0

# 4개로 분할해서 확인
def check_color_paper(m, color_paper): # m = (n/2)^k, color_paper = 색종이 중 확인할 부분
    global white_paper, blue_paper
    check = 0
    for i in range(m):
        for j in range(m):
            check += color_paper[i][j]
    if check == 0: # 전부 0이라면
        white_paper += 1
    elif check == m*m: # 전부 1이라면
        blue_paper += 1
    else: # 0과 1이 둘 다 있다면
        quarter_paper = [color_paper[i][0:m//2] for i in range(0, m//2)]
        check_color_paper(m//2, quarter_paper)
        quarter_paper = [color_paper[i][m//2:m] for i in range(0, m//2)]
        check_color_paper(m//2, quarter_paper)
        quarter_paper = [color_paper[i][0:m//2] for i in range(m//2, m)]
        check_color_paper(m//2, quarter_paper)
        quarter_paper = [color_paper[i][m//2:m] for i in range(m//2, m)]
        check_color_paper(m//2, quarter_paper)

check_color_paper(n, paper)
print(white_paper)
print(blue_paper)