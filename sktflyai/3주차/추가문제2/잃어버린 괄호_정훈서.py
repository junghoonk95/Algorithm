s = list(input().split('-'))
answer = 0
if s[0] == '': # 첫 시작이 음수인 경우
    for i in range(1, len(s)):
        s[i] = sum(list(map(int, s[i].split('+'))))
        answer -= s[i]
else: # 첫 시작이 양수인 경우
    for i in range(0, len(s)):
        s[i] = sum(list(map(int, s[i].split('+'))))
        if i == 0:
            answer += s[i]
        else:    
            answer -= s[i]

print(answer)