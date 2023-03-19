from itertools import*

print(*sorted([i for i in list(combinations([int(input()) for i in range(9)],7)) if sum(i)==100][0]), sep='\n')

#
