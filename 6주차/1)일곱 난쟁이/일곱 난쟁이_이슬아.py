dwarf=[]
for i in range(9):
    dwarf.append(int(input()))

dwarf.sort()
sum=0
legth=0

answer=[]

for i in range(9):
    sum=sum+dwarf[i]
 
legth=sum-100
delnum=0

for i in range(9):

    for j in range(i+1,9):
        if dwarf[i]+dwarf[j]==legth:
            delnum=dwarf[j]
            del dwarf[i]
            dwarf.remove(delnum)
            break
    if delnum!=0:
        break

for i in dwarf:
    print(i)
