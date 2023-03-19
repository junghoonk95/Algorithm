n = int(input())

count = 0
while n >= 0:
  if (n % 5) == 0: # 나눠 떨어진다면
    count += n // 5 # 몫
    print(count)
    break
  else: # 나눠 떨어지지 않는다면
    n -= 3 # 3kg
    count += 1

if n < 0:
  print(-1)