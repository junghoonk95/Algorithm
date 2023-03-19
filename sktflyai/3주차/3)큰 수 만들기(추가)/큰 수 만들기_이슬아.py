from collections import deque
def numchange(i,num,k,count):
    for j in range(i+1,len(num)):
        if count<k:
            if num[i]==num[j]:
                break
            elif num[i]>num[j]:
                num.remove(num[j])
                count=count+1
                break
            elif num[j]>num[i]:
                num.remove(num[i])
                count=count+1
                break
        return num

def solution(number, k):
    answer = ''
    maxnum=-1
    num=list(map(int,list(number)))
    count=0
    for i in range(len(num)):
        if count>=k:
            break
        numchange(i,num,k,count)

    answer=''.join(str(s) for s in num)
    return answer

  #예제만 성공..
