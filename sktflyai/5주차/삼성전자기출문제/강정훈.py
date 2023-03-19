########################디버깅중..........

import pprint
N,M,K=map(int,input().split())
arr=[[[(0,0,0)] for i in range(N)] for i in range(N)]
new_arr=[[[(0,0,0)] for i in range(N)] for i in range(N)]
for i in range(M):
    r,c,m,s,d=map(int,input().split())
    arr[r-1][c-1]=[(m,s,d)]
nx=[0,1,1,1,0,-1,-1,-1]
ny=[1,1,0,-1,-1,-1,0,1]
def move():
    global new_arr
    move_list=[]
    new_arr = [[[(0, 0, 0)] for i in range(N)] for i in range(N)]
    nx=[0,1,1,1,0,-1,-1,-1]
    ny=[1,1,0,-1,-1,-1,0,1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] != [(0, 0, 0)]:
                m,s,d=arr[i][j][0]
                move_list.append([(i+ny[d]*s)%N,(j+nx[d]*s)%N])
                new_arr[(i+ny[d]*s)%N][(j+nx[d]*s)%N].append((m,s,d))
    return new_arr,move_list


def meet(i,j,new_arr):
    temp=new_arr[i][j]

    tem_m=0
    tem_s=0
    tem_j=True #짝수
    for i in temp:
        tem_m=tem_m+i[0]
        tem_s=tem_s+i[1]
        if i[2]%2==1:
            tem_j=False

    if tem_j==True:
        tem_j=(0,2,4,6)
    else:
        tem_j=(1,3,5,7)

    return int(tem_m/5),int(tem_s/(len(temp)-1)), tem_j
arr_turn=[[[(0,0,0)] for i in range(N)] for i in range(N)]
for aa in range(K):

    move()

    for i in range(len(new_arr)):
        arr_turn = [[[(0, 0, 0)] for i in range(N)] for i in range(N)]
        for j in range(len(new_arr[i])):

            if len(new_arr[i][j])>=3:
                m_tem,s_tem,dir=meet(i,j,new_arr)
                for t in range(4):
                    arr_turn[i+ny[dir[t]]][j+nx[dir[t]]].remove((0,0,0))
                    arr_turn[i+ny[dir[t]]][j+nx[dir[t]]].append((m_tem,s_tem,dir[t]))
                    # arr_turn.pop(0)

                    new_arr=arr_turn.copy()
ans=0
# print(new_arr)
for i in new_arr:
    for j in i:
        for k in j:
            ans=ans+k[0]

print(ans)



''' 
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
2. 파이어볼은 4개의 파이어볼로 나누어진다.
3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
- 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
- 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
- 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
5. 질량이 0인 파이어볼은 소멸되어 없어진다.
-> 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자
'''

