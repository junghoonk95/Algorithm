# 시간초과 ㅠㅠ
# 찾아보니 combination 함수는 O(N! n^2!) 


from itertools import*
def solution(number, k):
    a= sorted(list(combinations(number, len(number)-k)),reverse=True)
    return "".join(a[0])
