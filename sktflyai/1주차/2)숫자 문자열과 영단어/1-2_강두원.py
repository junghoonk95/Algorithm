tb = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
'''
o, e, o, e, r, e, x, n, t, e
4, 3, 3, 5, 4, 4, 3, 5, 5, 4
'''
def solution(s):
    answer = ''
    
    c = 0
    while c < len(s):
        if s[c].isnumeric():
            answer += s[c]
            c += 1
        else:
            for i in range(3, 6):
                if s[c:c+i] in tb.keys():
                    answer += tb[s[c:c+i]]
                    c += i
                    break
    
    return int(answer)
