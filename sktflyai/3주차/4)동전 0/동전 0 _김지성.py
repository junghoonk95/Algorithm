# 입력
n,K = map(int,input().split())

#코인 종류 list 생성
coin_list = [input()for _ in range(n)]

# str 리스트로 저장
coin_list = list(map(int,coin_list))
coin_list.sort(reverse = True)

# 코인 개수
count = 0

# K를 리스트 처음부터 나눠준다
for i in coin_list:
    # 몫은 코인 개수 ( count에 올린다 ) 
    count += K//i
    # 나머지는 다시 돈에 넣어서 
    K = K%i
    
print(count)
