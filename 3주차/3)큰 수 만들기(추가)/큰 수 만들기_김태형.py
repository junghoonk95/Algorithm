def solution(number, k):
    st = []
    for i in range(len(number)):
        print(i)
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        print(number[i])
        st.append(number[i])
    print(st)
    return ''.join(st[:len(st) - k])
