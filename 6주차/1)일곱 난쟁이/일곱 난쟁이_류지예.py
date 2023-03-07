n = []
for _ in range(9):
  n.append(int(input()))
det = sum(n) - 100
re = []
n.sort()
cnt = 0
for i in n:
  if det - i in n:
    n.remove(i)
    n.remove(det - i)
    break

for i in n:
  print(i) 
