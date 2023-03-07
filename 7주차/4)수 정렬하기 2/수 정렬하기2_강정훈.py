def heapify(arr, idx, size):
    lar = idx
    l = 2 * idx +1  # 왼쪽
    r = 2 * idx + 2  # 오른쪽
    if l < size and arr[l] > arr[lar]:  # 왼쪽이 사이즈 보다 작고 / 값이 기준 큰값보다 zmaus lar=l
        lar = l
    if r < size and arr[r] > arr[lar]:
        lar = r
    if lar != idx:   #값이 달라지면 자리 바꾸기
        arr[lar], arr[idx] = arr[idx], arr[lar]
        heapify(arr, lar, size)

N=int(input())
number=[]
for i in range(N):
    number.append(int(input()))
n = len(number)

for i in range(n//2 - 1, -1, -1): #반에서 -1씩 -1까지
    heapify(number, i, n)


for i in range(n - 1, 0, -1):
    number[0], number[i] = number[i], number[0]  # 자리를 바꿔줌으로서 젤 큰 값을 맨 뒤
    heapify(number, 0, i)  # 맨 뒤로 보낸 값 빼고 다시 max heap으로 바꿔준다

print(*number,sep="\n")
