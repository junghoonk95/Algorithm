N=int(input())
init=N%5 # N의 나머지 최소값 이자 시작값

cnt=0
while cnt!=(N//5)+1: # 최대 N의 몫번 돌리기 -> 최대경우가 5의배수
    if init%3==0 or N <= 5  : # 시작값에서 5로 다나눴을때 나머지가 3으로 나눠지면 -> 끝 3한번이용
        cnt=cnt+1
        break
    else:
        init=init+5 # 아니면 나머지에 5 추가 숫자3 2+ 이용
        cnt=cnt+1
    cnt=cnt+1


if init == N:
    if init%3==0:   #다 돌렸을때 init이 N 이면 3의배수

        print(N//3)
    else:
        print(-1)  # 3의 배수아니면 불가능 -1 출력
else:
    print(cnt+(N-3*cnt)//5)  # 3번 이용 횟수 + (N-3*이용 회수)를 5로 나눈
