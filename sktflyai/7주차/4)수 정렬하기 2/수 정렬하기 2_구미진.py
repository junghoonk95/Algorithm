# https://maktubi.tistory.com/258

# 합병정렬
import sys
input = sys.stdin.readline

n = int(input())
list = [int(input().rstrip()) for _ in range(n)]

# 합병 정렬
def mergeSort(list):
    if len(list) <= 1:
        return list
    
    # 1) Divide - 배열 반으로 나누기
    mid = len(list) // 2

    # 2) Conquer - 나뉜 배열들을 각각 정렬하기
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid+1:])

    # 3) Combine - 다시 하나의 배열로 합치기
    merge(left, right)

def merge(left, right):
    sorted = []
    p1, p2 = 0, 0 # 나뉜 배열 2개를 각각 가리키는 인덱스

    while len(left) > p1 and len(right) > p2:
        if left[p1] > right[p2]:
            sorted.append(right[p2])
            p2 += 1
        else:
            sorted.append(left[p1])
            p1 += 1
        
    while len(left) > p1 and len(right) <= p2:
        sorted.append(left[p1])
        p1 += 1
    
    while len(right) > p2 and len(left) <= p1:
        sorted.append(right[p2])
        p2 += 1

mergeSort(list)

for i in sorted:
    print(i)
