import itertools

n = int(input())
inputs=list(map(int,input().split()))
n_op = list(map(int,input().split()))

operators="+-*/"
op=""
for o,num in zip(operators,n_op):
    op+=o*num
    
op_per=list(itertools.permutations(op,n-1))

outputs=[]

for op in op_per:
    result=inputs[0]
    for o,i in zip(op,inputs[1:]):
        if o == "+":
            result+=i
        elif o == "-":
            result-=i
        elif o == "*":
            result*=i
        else :
            result = int(result / i)
    outputs.append(result)

print(max(outputs))
print(min(outputs))
