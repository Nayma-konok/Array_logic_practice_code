nums=[3,10, 4, 5, 6]

#first element, Last element, Middle elements
print(nums[0])
print(nums[-1])

middle=len(nums)//2
print(middle)
print(nums[2])


#Replace the value at index 2 with 100.
nums[2]=100
print(nums)

#Swap the first and last elements of a list.
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)