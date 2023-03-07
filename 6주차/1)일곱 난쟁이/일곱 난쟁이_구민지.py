import itertools

heights=[int(input()) for _ in range(9)]
comb = list(itertools.combinations(heights,7))

for c in comb :
    if sum(c)==100:
        for num in sorted(c):
            print(num)
        break
