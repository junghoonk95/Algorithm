def solution(brown, yellow):
    for i in range(yellow,0,-1):
        if 2*(i+2)+yellow/i*2==brown:
            return [i+2,yellow/i+2]
            
