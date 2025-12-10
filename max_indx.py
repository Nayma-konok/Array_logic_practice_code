nums=[10,3,9,7,4]

l=float("-inf")
l_index=-1

for i,num in enumerate(nums):
    if num>l:
        l=num
        l_index=i
print(l_index)
