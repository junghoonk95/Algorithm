a = [int(input()) for _ in range(9)]
remain = sum(a) - 100
fake = []
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == remain:
            fake.append(a[i])
            fake.append(a[j])
            break
    if len(fake) == 2:
        break
a.sort()
for i in a:
    if i not in fake:
        print(i)
