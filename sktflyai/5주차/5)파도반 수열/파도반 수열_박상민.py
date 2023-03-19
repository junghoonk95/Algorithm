lst = [0, 1, 1, 1, 2]

for _ in range(int(input())):
    n = int(input())
    try:
        print(lst[n])
    except:
        while len(lst) != (n+1):
            lst.append(lst[-1] + lst[-5])
        print(lst[-1])
