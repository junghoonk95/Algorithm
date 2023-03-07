def solution(s):
    answer = len(s)
    if len(s) == 1:
        answer = 1
    else:
        for l in range(1, len(s)//2 + 1):     
            cur_size = len(s)
            count = 0
            pre = s[0:l]
            for i in range(l, len(s)-l+1, l):
                if pre != s[i:i+l]:
                    if count > 0:
                        cur_size += len(str(count+1))
                    cur_size -= count*l
                    count = 0
                else:
                    count += 1

                pre = s[i:i+l]
            
            if count > 0:
                cur_size += len(str(count+1))
                cur_size -= count*l
            
            answer = min(answer, cur_size)

    return answer
