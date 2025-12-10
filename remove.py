nums =  [0,1,2,2,3,0,4,2]

k = 0   # index to place next valid number
val=2
for num in nums:
    if num != val:
        nums[k] = num
        k += 1

print(k)
    
