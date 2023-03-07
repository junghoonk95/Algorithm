def solution(n,a,b):
    round = 0
    while a != b:
        a = a//2 + a%2
        b = b//2 + b%2
        round += 1

    return round
