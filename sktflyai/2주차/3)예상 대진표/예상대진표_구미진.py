import math
def solution(n,a,b):
    answer = 1
    x = min(a, b)
    y = max(a, b)

    while True:
        if (y - x == 1) and (x % 2 == 1):
            break
        # 1이 아닐 때만 번호가 바뀜
        if x != 1:
            x = math.ceil(x/2)
        if y != 1:
            y = math.ceil(y/2)
        answer += 1
    return answer

# 2로 나누고 올림하기

# 테스트 케이스
print(solution(8, 4, 7)) # 3
print(solution(8, 8, 7)) # 1
print(solution(8, 4, 5)) # 3