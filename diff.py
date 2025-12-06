nums=[10,3,9,7,4]

largest=nums[0]
smallest=nums[-1]

for num in nums:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num

diff=largest-smallest

print(largest)
print(smallest)
print(diff)