people = [70, 50, 80, 50]
limit = 100
max_cnt = 2
rescue = 0
remain_w = [] #limit 값에서 각 people의 무게를 뺀 값
people_idx = [] # people의 인덱스 값을 저장한 값

for weight in people:
    remain = limit-weight
    remain_w.append(remain)
print(remain_w)
    
for i in range(len(people)):
    people_idx.append(i)      
print(people_idx)

dic = {ori_idx:remain_w for ori_idx, remain_w in zip(people_idx, remain_w)}
# people의 원소값과, remain의 원소값을 딕셔너리로 저장
print(dic)
sorted_remain_w = sorted(remain_w) 
print(sorted_remain_w)

while True:     
    print('sorted_check', sorted_remain_w)
    a, b = sorted_remain_w[-(max_cnt):] # >> 뒤에서 두개가 해당 리스트에서 가장 작은 값
    print(a, b)
    if a+b >= limit: # >> 이 둘을 더한 값이 limit 값 보다 작거나 같으면 
        # for key, value in dic.items(): 
        #     # 해당 값을 가지는 remain의 index를 찾아 접근하기 위해 딕셔너리 접근 (remain idx = people idx)
        #     # print(value)
        #     if value == a:    
        #         # print(key)
        #         idx_a = key
        #     if value == b:
        #         # print(key)
        #         idx_b = key
        people.remove(people[-1])   #해당 값을 people, sorted_remain_w 리스트에 접근해 원소 제거
        sorted_remain_w.remove(sorted_remain_w[-1])
        print('1', people)
        print('1', sorted_remain_w)
        # print(people[3])
        people.remove(people[-2])   
        sorted_remain_w.remove(sorted_remain_w[-1])
        print('2', people)
        rescue +=1                 
        # 제거가 완료되면 rescue(구조) +1 
        sorted_remain_w = sorted(sorted_remain_w) 
        # 남은 원소들을 갖고있는 sorted_remain_w 리스트 재정렬 
    
    else: # 예외처리 ... 
        for i in people:
            print(i)
            if i > (limit//2):
                rescue +=1
                people.remove(i)
        

#     # for _ in people:
# #     #     rescue+=1                
#     if len(people)==0:
#         break
rescue