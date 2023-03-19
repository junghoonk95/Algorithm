sugar = int(input())

res = 0
while sugar >= 0 : 
    if sugar % 5 == 0 :  # 5의 배수이면
        res += (sugar // 5)  # 5로 나눈 몫 == 들고 간 봉지의 개수
        print(res)
        break
    sugar -= 3  # 5의 배수가 될 때까지 설탕 값 -3, 봉지의 개수 +1
    res += 1  
else:
    print(-1)