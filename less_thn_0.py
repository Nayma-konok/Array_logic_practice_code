nums=[10,-3,9,-7,4,-5]

for num in nums[:]:
    if num<0:
        nums.remove(num)
# nums = [num for num in nums if num >= 0]
print(nums)