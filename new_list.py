#1.Given a list, create a new list where each value is doubled.Example: [1,2,3] → [2,4,6]

nums=[1,2,3]
new_nums=[]
i=0
for i,num in enumerate(nums):
    num=nums[i]*2
    new_nums.append(num)
    i+=1
print(new_nums)