def solution(n,a,b):
    # a와 b중 b를 더 크게
    # 라운드 진행할 때마다 2씩 나눈다
    # a와 b가 만나는 라운드에서 결과 도출
    answer = 1
    if a>b:
        a,b=b,a
        
    while(1):
        if a%2 ==1 and a+1 ==b:
            return answer
        if a%2 ==1:
            a = a//2 + 1
        else:
            a = a//2
        if b%2 ==1:
            b = b//2 +1
        else:
            b = b//2
        answer+=1

    return answer
