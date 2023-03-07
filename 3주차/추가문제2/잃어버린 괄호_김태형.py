equation = list(input())
is_processing = False
for i in range(len(equation)):
    # if is_processing:
    if equation[i] == '-':
        equation[i] = ','

equation = "".join(equation).split(",")
answer = sum(list(map(int,equation[0].split("+"))))
for numbers in equation[1:]:
    answer -= sum(list(map(int,numbers.split("+"))))

print(answer)
