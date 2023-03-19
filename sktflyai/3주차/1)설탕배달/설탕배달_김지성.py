n = int(input())
answer = 0

while(1):
    if n>0: #남은 설탕키로수가 있을 때
        if n==1 or n==2: #3과 5로 나타낼 수 없는 숫자일 때
            print(-1)
            break
        else: #3과 5로 나눠질 가능성이 있는 숫자일 때
            if n%5==0: # n이 5로 나눠질 때
                answer += n/5
                print(int(answer))
                break
            elif n%5!=0: # n이 5로 나눠지지 않을 때
                # 3 빼주기 , 봉지 하나 추가 ( 3키로짜리 )
                n -= 3
                answer +=1
    elif n==0: # 남은 설탕 키로수가 없을 때
        print(int(answer))
        break
    elif n<0:
        print(-1)
        break
