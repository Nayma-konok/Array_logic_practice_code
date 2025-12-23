nums = [0,1,0,3,12]

s=0

for i,num in enumerate(nums):
    if num!=0:
        nums[i], nums[s] = nums[s], nums[i]
        s+=1
        
print(nums)