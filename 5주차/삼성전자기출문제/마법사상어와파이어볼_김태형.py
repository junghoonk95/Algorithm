'''
NxN 격자
파이어볼 M개

'''
from collections import defaultdict

# N : 격자, M : 파이어볼, K : 실행 횟수
N,M,K = map(int,input().split()) 

# r,c : 위치 ,m : 질량,s : 속력, d : 방향

f_balls = [list(map(int,input().split())) for _ in range(M)] 

for i in range(len(f_balls)):
    r,c,m,s,d = f_balls[i]
    f_balls[i] = [r-1,c-1,m,s,d]
# 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

pos = defaultdict(list)
# 1.모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
def move():
    for i in range(len(f_balls)):
        r,c,m,s,d = f_balls[i]

        nr = r + dr[d]*s + N*s
        nc = c + dc[d]*s + N*s

        nr %= N
        nc %= N
        f_balls[i] = [nr,nc,m,s,d]

# 2.이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.

def get_balls():
    global pos
    pos = defaultdict(list)

    for i in range(len(f_balls)):
        r,c,_,_,_ = f_balls[i]
        # rc = ",".join(map(str,[r,c]) 
        pos[(r,c)].append(f_balls[i]) # dictionary의 key 값으로 tuple을 전달할 수 있음

def process_balls():
    global f_balls
    tmp = []
    for key in pos.keys():
        if len(pos[key]) >= 2:
            tmp_r,tmp_c = key
            tmp_m,tmp_s,tmp_d = 0,0,[]
            tmp_balls = pos[key]
            for _,_,m,s,d in tmp_balls:
                tmp_m += m
                tmp_s += s
                tmp_d.append(d%2)
            # 2-3-1. 질량 : sum(파이어볼질량)/5
            tmp_m //= 5
            # 2-3-2. 속력 : sum(파이어볼속력)/합쳐진 파이어볼 개수
            tmp_s //=len(tmp_balls)
            # 2-3-3. 방향 : 합쳐지는 방향 모두 홀수 or 짝수 -> 0,2,4,6 else 1,3,5,7
            tmp_d = set(tmp_d)
            tmp_d = [0,2,4,6] if len(tmp_d) == 1 else [1,3,5,7]
            # 2-4. 질량 0인 파이어볼 소멸 <- 2-3-1에서 반올림해야되는지 확인
            if tmp_m == 0:
                continue
            for d in tmp_d:
                tmp.append([tmp_r,tmp_c,tmp_m,tmp_s,d])
        elif len(pos[key]) == 1:
            tmp += pos[key]
    f_balls = tmp

# 3.마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.
def get_answer():
    answer = 0
    for _,_,m,_,_ in f_balls:
        answer += m
    print(answer)

# main
for z in range(K):
    move()
    get_balls()
    process_balls()

get_answer()