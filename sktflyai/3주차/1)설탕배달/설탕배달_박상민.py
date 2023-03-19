sugar = int(input())
cnt = -1

remainder = sugar % 5 # 5로 나누어 나머지를 확인

while sugar >= remainder: # 계속해서 더하는 것을 방지하기 위함
    if remainder % 3 == 0: # 5의 나머지 와 3의 나머지가 모두 0이면 탈출
        cnt = remainder // 3 + (sugar - remainder) // 5 # 나머지를 3으로 나눈 몫과 5로 나눈 몫을 더한 값이 가방의 개수이다.
        break
    else:
        remainder += 5
print(cnt) # while문의 break부분이 작동한 경우는 양수의 cnt가 출력되고 조건문으로 탈출한 경우는 -1이 그대로 출력되게끔 만듦.
