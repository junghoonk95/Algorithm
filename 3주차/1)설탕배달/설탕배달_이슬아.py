def sugar(n):
    count=0
    
    while n>0:
        if n%5==0:
            count=count+(n//5)
            n=0
            break
        n=n-3
        count=count+1
    if n<0:
        count=-1
    return count

weight=int(input())

print(sugar(weight))
