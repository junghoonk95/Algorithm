from collections import deque

def solution(people, limit):

    people.sort()
    people = deque(people) # deque로 타입변경
    l = 0; r = len(people) - 1 # people deque의 양옆 위치를 잡아줄 변수 선언
    boat = deque() # 쌍을 이루거나 홀로 들어갈 인원의 인덱스를 담아 마지막에 길이를 반환시켜줄 deque
    while True: # l이 r보다 커지거나 같아지면 탈출하는 반복문
        if r > l:
            if people[r] + people[l] <= limit: # 최대 값과 최솟값이 한계보다 낮거나 같은 경우 튜플로 쌍을 이뤄 boat에 append시켜준다.
                boat.append((l, r))
                r -= 1
                l += 1
            else:
                boat.append(r) # 한계를 넘은 경우 최대값만 담아준다.
                r -= 1
        elif r == l: # 가운데에서 만나는 경우 보트에 추가해주고 탈출
            boat.append(r)
            break
        else: # l이 r보다 커지는 경우 탈출
            break
    answer = len(boat)

    return answer
