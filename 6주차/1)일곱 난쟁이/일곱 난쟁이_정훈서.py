nums = []
for _ in range(9):
    nums.append(int(input()))
total = sum(nums)
print("total", total)
tmp = 0
for i in range(8):
    for j in range(i+1, 9):
        tmp = total - nums[i]
        tmp -= nums[j]
        print("tmp", tmp)
        if tmp == 100:
            rm1, rm2 = nums[i], nums[j]
            print(rm1, rm2)
            nums.remove(rm1)
            nums.remove(rm2)
            nums.sort()
            break
    if len(nums) == 7:
        break
for num in nums:
    print(num)
    
# 3
# 4
# 5
# 6
# 7
# 10
# 15
# 20
# 40