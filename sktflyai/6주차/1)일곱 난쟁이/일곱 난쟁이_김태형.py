# 1번
from itertools import combinations as cb

heights = []

for _ in range(9):
    heights.append(int(input()))

list_cb = list(cb(heights,7))

for numbers in list_cb:
    if sum(numbers) == 100:
        numbers = list(numbers)
        numbers.sort()
        for number in numbers:
            print(number)
        break