nums=[10,3,9,7,4]

largest=float("-inf")
largest_2=float("-inf")

for num in nums:
    if num>largest:
        largest_2=largest
        largest=num
    elif num>largest_2 and num!=largest:
        largest_2=num

print(largest_2)