nums=[3,10,3,4,9,7,4]

d=set()

for num in nums:
    if num in d:
        print(num)
        break
    d.add(num)

