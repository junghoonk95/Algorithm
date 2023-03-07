N = int(input())
meetings = []
cnt = 0

for i in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
meeting_end = 0

for i in meetings:
    start = i[0]
    end = i[1]
    
    if start >= meeting_end:
        cnt+=1 
        meeting_end = end
print(cnt)