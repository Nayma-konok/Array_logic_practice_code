#Count how many times a specific value appears
numbers=[3,10, 4,3, 5, 6]

target=3
count=0
nums=[]

for num in  numbers:
    if num==target:
        count+=1
        nums.append(num)
    
print(nums)
print(count)    