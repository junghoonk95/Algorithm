def solution(nums):
    a=len(set(nums))
    
    if a<=len(nums)/2:
        return a
    else:
        return len(nums)/2
