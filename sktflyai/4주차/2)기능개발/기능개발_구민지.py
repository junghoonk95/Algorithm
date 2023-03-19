import math

def solution(progresses,speeds):
    
    sub_list=[]
    for p,s in zip(progresses,speeds):
        temp=math.ceil((100-p)/s)
        sub_list.append(temp)
        
    temp=[]
    ans=[]
    while(sub_list):
        num = sub_list.pop(0)
        if temp:
            if temp[0]<num:
                ans.append(len(temp))
                temp=[]
                temp.append(num)
                continue
        temp.append(num)
    ans.append(len(temp))
    return ans
