def solution(number, k):
    answer = ''
    n = list(number)
    index = 0 # 초기값
    for i in range(len(number)-k):
        answer += max(n[index:k+i+1])
        index += n[index:k+i+1].index(answer[-1]) + 1

    print(answer)

    # test case 10번에서 시간초과 남 ㅠㅡㅠ