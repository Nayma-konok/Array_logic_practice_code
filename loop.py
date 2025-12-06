nums=[3,10, 4, 5, 6,11]
 
#Calculate the total sum of all numbers in a list.
total=0
for num in nums:
    total=num+total

# print(sum)

#Count how many numbers in a list are even.
count=0
for num  in nums:
    if num%2==0:
        count+=1
print(count)

#Count how many numbers are greater than 10.
count=0
for num  in nums:
    if num>10:
        count+=1

print(count)
    
#Print all numbers at even indexes (0, 2, 4...)
for i,num  in enumerate(nums):
    if i%2==0:
        print(num)

#Print all numbers at odd indexes.
for i,num  in enumerate(nums):
    if i%2!=0:
        print(num)