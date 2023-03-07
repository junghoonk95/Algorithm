def solution(number, k):
    ans = []
    while k > 0 and len(number) > 0:
        max_num = max(number[:k+1])
        ans.append(max_num)
        max_idx = number.index(str(max_num))
        number = number[max_idx+1:]
        k -= max_idx
    ans += number
    if k > 0:
        ans.pop()
    return ''.join(ans)

'''
1. 앞에서부터 k+1개의 숫자 슬라이싱
2. 슬라이싱한 문자열 중 가장 큰 숫자 앞에 있는 숫자들 제거
3. 가장 큰 숫자 다음 숫자부터 다시 k+1개의 숫자 슬라이싱
-> k가 0이 될 때까지 반복
'''