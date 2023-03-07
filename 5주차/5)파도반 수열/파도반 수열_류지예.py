import math

t = int(input())
n_list = []
for _ in range(t):
  n_list.append(int(input()))
result = []

def pado(x):
  global result
  plus = [1, 0, 0, 1]
  sum = 0
  for _ in range(math.ceil(x/4)):
    start = []
    for i in range(4):
      start.append(sum)
      sum += plus[i]
      plus[i] = sum
      result.append(sum)
    plus = start
  return result

pado(max(n_list))
for i in n_list:
  print(result[i-1], end='\n')
