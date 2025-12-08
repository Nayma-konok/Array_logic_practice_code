nums=[1,2,3,4,4,5]
seen=set()
first_repeated=False

for num in nums:
    if num in seen:
        first_repeated=True
        break
    seen.add(num)

print(first_repeated)